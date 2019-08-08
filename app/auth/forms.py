#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: forms.py
Description: 
Author: Barry Chow
Date: 2019/7/26 5:40 PM
Version: 0.1
"""
from flask_wtf import Form
from wtforms import SubmitField,StringField,BooleanField,PasswordField
from wtforms.validators import Required,Length,Email,Regexp,EqualTo
from ..models import User
from wtforms import ValidationError

class LoginForm(Form):
    email = StringField('Email',validators=[Required(),Email(),Length(1,64)])

    password = PasswordField('Password',validators=[Required()])
    remember_me = BooleanField('keep me logged in')
    submit = SubmitField('Log In')


class RegistrationForm(Form):
    email = StringField('Email',validators=[Required(),Length(1,64),Email()],
                        )
    username = StringField('Username',validators=[Required(), Length(1, 64),
                                                  Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                               'Usernames must have only letters, ''numbers, dots or underscores')])
    password = PasswordField('Password',validators=[
        Required(),EqualTo('password2',message='Password must match.'),
    ])
    password2 = PasswordField('Password',validators=[Required()])
    submit = SubmitField('Register')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class ChangePasswordForm(Form):
    old_password = PasswordField('Old password', validators=[Required()])

    password = PasswordField('New Password', validators=[
        Required(), EqualTo('password2', message='Password must match.'),
    ])
    password2 = PasswordField('Confirm Your Password', validators=[Required()])
    submit = SubmitField('Change Password')

