#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: manage.py
Description: 
Author: Barry Chow
Date: 2019/7/26 4:19 PM
Version: 0.1
"""

import os
from app import create_app,db
from app.models import User,Role,Post
from flask_script import Manager,Shell
from flask_migrate import MigrateCommand,Migrate

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app,db)

def make_shell_context():
    return dict(app=app,db=db,User=User,Role=Role,Post=Post)

manager.add_command('shell',Shell(make_context=make_shell_context))
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    '''run the unit tests'''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def reset():
    '''reset flask server'''
    from app.models import User,Role,Post
    from app import db
    db.drop_all()
    db.create_all()
    Role.insert_roles()
    User.generate_fake(100)
    Post.generate_fake(100)

@manager.command
def deploy():
    '''deploy the flask'''
    from app.models import User,Role,Post
    from app import db
    db.drop_all()
    db.create_all()
    Role.insert_roles()

if __name__ == '__main__':
    manager.run()

