#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Django database settings
"""
from __future__ import absolute_import


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'knittygritty_db',                      # Or path to database file if using sqlite3.
        'USER': 'knittygritty',                      # Not used with sqlite3.
        'PASSWORD': 'knitting4SEX',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}