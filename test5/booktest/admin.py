# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import *

# @admin.register(BookInfo)
# class BookInfoAdmin(admin.ModelAdmin):
#     list_display=['id','btitle','bpub_date']
#admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(Test1)