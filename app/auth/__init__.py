#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: __init__.py.py
Description: 
Author: Barry Chow
Date: 2019/7/26 5:12 PM
Version: 0.1
"""
from flask import Blueprint
auth = Blueprint('auth',__name__)

from . import views
