#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module name
"""
from __future__ import absolute_import
from django.db import models
from django.db.models import fields
import os


class Product(models.Model):
    name = fields.CharField(max_length=250)
    description = fields.TextField()

    def __unicode__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images')
    width = fields.IntegerField(blank=True)
    height = fields.IntegerField(blank=True)
    image = models.ImageField(upload_to='product/images', width_field='width', height_field='height')

    def __unicode__(self):
        return '%(product)s - %(image)s' % {
            'product': self.product, 'image': os.path.basename(self.image.path)
        }