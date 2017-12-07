# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

# Create your models here.

# class UserInfo(models.Model):
#     uname=models.CharField(max_length=10)
#     upwd=models.CharField(max_length=40)
#     isDelete=models.BooleanField()
#
#
# class BookInfo(models.Model):
#     btitle = models.CharField(max_length=20)
#     bpub_date = models.DateTimeField(db_column='pub_date')
#     bread = models.IntegerField(default=0)
#     bcoment = models.IntegerField(null=False)
#     isDelete = models.BooleanField(default=False)
#
#
# class HeroInfo(models.Model):
#     hname = models.CharField(max_length=10)
#     hgender = models.BooleanField(default=True)
#     isDelete = models.BooleanField(default=False)
#     hcontent = models.CharField(max_length=1000)
#     book = models.ForeignKey(BookInfo)

class AreaInfo(models.Model):
    title=models.CharField(max_length=20)
    parea=models.ForeignKey('self',null=True,blank=True)

class Test1(models.Model):
    content = HTMLField()