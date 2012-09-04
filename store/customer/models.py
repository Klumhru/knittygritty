#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
store.customer.models
"""
from __future__ import absolute_import


from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields

class Customer(models.Model):
    user = models.ForeignKey(User, related_name='customer')

