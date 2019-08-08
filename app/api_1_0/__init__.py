#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: __init__.py.py
Description: 
Author: Barry Chow
Date: 2019/7/29 9:17 PM
Version: 0.1
"""
from flask import Blueprint
api = Blueprint('api',__name__)
from . import authentication,comments,posts,decorators,errors,users
