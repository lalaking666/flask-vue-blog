#!/usr/bin/env python
# encoding: utf-8

#SQLALCHEMY_DATABASE_URI = "sqlite:///./test.db"
SQLALCHEMY_DATABASE_URI = 'sqlite:///./test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = "123456"

BCRYPT_LEVEL = 13

TOKEN_EXPIRATION_TIME = 12000  # 单位是秒
