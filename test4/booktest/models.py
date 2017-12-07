# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BookInfo(models.Model):
    btitle=models.CharField(max_length=20)
    bpub_data=models.DateTimeField(db_column='pub_datae')
    bread=models.IntegerField()
    bcomment=models.IntegerField()
    isDelete=models.BooleanField()
    class Meta():
        db_table='bookinfo'

class HeroInfo(models.Model):
    hname=models.CharField(max_length=10)
    hgender=models.BooleanField()
    hcontent=models.CharField(max_length=1000)
    isDelete=models.BooleanField()
    book=models.ForeignKey('BookInfo')
    def showname(self):
        return self.hname