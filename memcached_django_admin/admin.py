#-*- coding: utf-8 -*-
from django.contrib import admin
from memcached_django_admin.models import MemcachedKey


class MemcachedAdmin(admin.ModelAdmin):
    pass

admin.site.register(MemcachedKey, MemcachedAdmin)
