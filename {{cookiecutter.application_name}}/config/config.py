# -*- coding: utf-8 -*-
import os

class Config(object):
    APP_ROOT = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_ROOT, os.pardir))
    SECRET_KEY = os.environ['SECRET_KEY']

class DevelopmentConfig(Config):
    DEBUG = True
    WTF_CSRF_ENABLED = False

class TestConfig(Config):
    TESTING = True
