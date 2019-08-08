#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: errors.py
Description: 
Author: Barry Chow
Date: 2019/7/29 10:05 PM
Version: 0.1
"""
from flask import request,jsonify

def forbidden(message):
    response = jsonify({'error':'forbidden','message':message})
    response.status_code = 400
    return response

def unauthorized(message):
    response = jsonify({'error':'unauthorized','message':message})
    response.status_code = 401
    return response


def forbidden_error(message):
    response = jsonify({'error':'forbidden','message':message})
    response.status_code = 403
    return response