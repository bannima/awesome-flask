#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: decrators.py
Description: 
Author: Barry Chow
Date: 2019/7/27 2:56 PM
Version: 0.1
"""
from functools import wraps
from flask import abort
from flask_login import current_user
from .models import Permission

def permission_required(permission):
    def decrator(f):
        @wraps(f)
        def decrator_function(*args,**kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args,**kwargs)
        return decrator_function
    return decrator

def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)
