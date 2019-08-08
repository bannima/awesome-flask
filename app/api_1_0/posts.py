#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: posts.py
Description: 
Author: Barry Chow
Date: 2019/8/5 2:55 PM
Version: 0.1
"""
from . import api
from ..auth import auth
from ..models import Post
from flask import jsonify,url_for
from flask_httpauth import HTTPBasicAuth
from flask import g


auth = HTTPBasicAuth()

@api.route('/posts')
def get_posts():
    posts= Post.query.all()
    try:
        res = jsonify({'posts':[ \
        post.to_json() for post in posts]})
    except Exception as e:
        res = e
    return res

@api.route('/posts/<int:id>')
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify(post.to_json())

