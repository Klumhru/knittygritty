#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Django settings compiler
"""
from __future__ import absolute_import

from . common import *
from . staticfiles import *
from . database import *
from . logging import *

try:
    from . development import *
except ImportError:
    pass