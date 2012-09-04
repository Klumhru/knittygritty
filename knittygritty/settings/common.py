#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Django common settings
"""
from __future__ import absolute_import

import os

ROOT = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Högni Gylfason', 'klumhru@gmail.com'),
    ('Amy Tucker', 'zamalynn@gmail.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = '))h(71e0@%*0kzh#i=u%b0rbt%ah4w*sr%nvg(_40xazkds3l('

from . structure import *