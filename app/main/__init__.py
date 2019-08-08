#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: __init__.py.py
Description: 
Author: Barry Chow
Date: 2019/7/26 4:19 PM
Version: 0.1
"""
from flask import Blueprint
main = Blueprint('main',__name__)
from ..models import Permission
from . import views,errors

@main.app_context_processor
def inject_permission():
    return dict(Permission=Permission)