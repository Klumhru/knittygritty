#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module name
"""
from __future__ import absolute_import
from __builtin__ import object

from django.db import models
from django.db.models import fields
from store.customer.models import Customer
from store.product.models import Product


class Order(models.Model):
    customer = models.ForeignKey(Customer)

    def __unicode__(self):
        return self.customer.user.get_full_name() + " Order(" + self.id + ")"

class ProductOrder(models.Model):
    product = models.ForeignKey(Product)
    order = models.ForeignKey(Order, related_name='products')
    number = fields.IntegerField()

    def __unicode__(self):
        return "%(number)i %(product_name)s by %(customer_name)s in Order(%(order_id)i)" % {
            'number': self.number, 'product_name': self.product.name,
            'customer_name': self.order.customer, 'order_id': self.order.id
        }
