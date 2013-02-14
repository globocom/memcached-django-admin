#-*- coding: utf-8 -*-
from django.db import models
from django.core.cache import cache


class MemcachedKey(models.Model):
    id = models.AutoField(primary_key=True, db_column="memcached_key_id")
    key = models.TextField(db_column="key_txt", verbose_name=u"Memcached Key",
                           null=False, blank=False)

    class Meta:
        db_table = "memcached_key"
        app_label = 'memcached'

    def save(self, *args, **kwargs):
        cache.delete(self.key)

        super(MemcachedKey, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.key
