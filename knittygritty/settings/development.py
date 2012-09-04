#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module name
"""
from __future__ import absolute_import


from . import common

def concat_tuple(tup, *args):
    a = [t for t in tup]
    for arg in args:
        a.append(arg)
    return a

INSTALLED_APPS = concat_tuple(common.INSTALLED_APPS,
    'debug_toolbar',
    'devserver',
)

MIDDLEWARE_CLASSES = concat_tuple(common.MIDDLEWARE_CLASSES,
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'devserver.middleware.DevServerMiddleware',
)

INTERNAL_IPS = ('127.0.0.1',)
