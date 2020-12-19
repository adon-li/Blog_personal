#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Liyd
# @Time : 2020/12/16 17:42
# @Email   : muziyadong@gmail.com
# @Software: PyCharm
from .base import *  #NOQA
DEBUG=True

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER':'root',
        'PASSWORD':'root',
        'HOST':'127.0.0.1',
        'port':3306,
        'OPTIONS':{'charset':'utf8mb4'}
    }
}

