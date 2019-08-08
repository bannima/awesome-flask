#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: email.py
Description: 
Author: Barry Chow
Date: 2019/7/26 8:42 PM
Version: 0.1
"""
from threading import Thread
from flask import current_app,render_template
from flask_mail import Message
from . import mail

def send_async_mail(app,msg):
    with app.app_context():
        mail.send(msg)

def send_mail(to,subject,template,**kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX']+' '+subject,
                  sender=app.config['FLASKY_MAIL_SENDER'],
                  recipients=[to])
    msg.body = render_template(template+'.txt',**kwargs)
    msg.html = render_template(template+'.html',**kwargs)
    thr = Thread(target=send_async_mail,args=[app,msg])
    thr.start()
    return thr


