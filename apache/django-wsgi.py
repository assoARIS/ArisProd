#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 16:26:53 2022

@author: jmichel
"""

import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'ArisDevt.settings'

path = '/home/jmichel/ArisDevt'
if path not in sys.path:
    sys.path.append(path)

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()