#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: __init__.py.py
Description: 
Author: Barry Chow
Date: 2019/7/26 4:18 PM
Version: 0.1
"""
from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_pagedown import PageDown


from flask_login import LoginManager

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

#login
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view ='auth.login'

pagedown = PageDown()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    #additional route and error page
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/auth')

    #login
    login_manager.init_app(app)

    #pagedown
    pagedown.init_app(app)

    #register api
    from .api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint,url_prefix='/api/v1.0')

    return app