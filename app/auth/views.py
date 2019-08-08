#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: views.py
Description: 
Author: Barry Chow
Date: 2019/7/26 5:13 PM
Version: 0.1
"""
from datetime import datetime
from flask import render_template,redirect,url_for,request,flash
from . import auth
from ..models import User
from .forms import LoginForm
from flask_login import login_user
from flask_login import logout_user,login_required
from .forms import RegistrationForm
from .. import db
from ..email import send_mail
from flask_login import current_user
from .forms import ChangePasswordForm

@auth.route('/login',methods =['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('invalid username or password')

    return render_template('auth/login.html',form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you have been logged out.')
    return redirect(url_for('main.index'))

@auth.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password = form.password.data,
                    member_since = datetime.utcnow(),
                    last_seen = datetime.utcnow())
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_mail(user.email,'Confirm Your Account',
                  'auth/email/confirm',user=user,token=token)
        flash('A confirmation email has been sent to you by email')
        return redirect(url_for('main.index'))

    return render_template('auth/register.html',form=form)

@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash('You have confirmed your account. Thanks!')
    else:
        flash('The confirmation link is invalid or has expired.')
    return redirect(url_for('main.index'))

@auth.before_app_request
def before_request():
    if current_user.is_authenticated\
            and not current_user.confirmed \
            and request.endpoint[:5]!='auth.'\
            and request.endpoint!='static':
        return redirect(url_for('auth.unconfirmed'))

@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')

@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_mail(current_user.email,'Confirm Your Account',
              'auth/email/confirm',user=current_user,token=token)
    flash('A new confirmation email has been sent to you by email')
    return redirect(url_for('main.index'))


@auth.route('/change_password',methods=['GET','POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.password.data
            db.session.add(current_user)
            flash('The password has been changed')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid Password')
    return render_template('auth/change_password.html',form=form,username=current_user.username)

@auth.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.ping()
        if not current_user.confirmed \
                and request.endpoint[:5]!='auth.':
            return redirect(url_for('auth.unconfirmed'))