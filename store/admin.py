#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module name
"""
from __future__ import absolute_import


from django.contrib import admin
from store.customer.models import Customer
from store.order.models import Order
from store.product.models import Product, ProductImage


class CustomerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Customer, CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass

class ProductImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Order, OrderAdmin)