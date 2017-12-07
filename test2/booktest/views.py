# -*- coding: utf-8 -*-
from __future__ import unicode_literals



# Create your views here.
from django.shortcuts import render
from models import *
from django.db.models import Max, F, Q

def index(request):
    # list = BookInfo.books1.filter(heroinfo__hcontent__contains='八')
    # list = BookInfo.books1.filter(pk__lte=3)
    # Max1=BookInfo.books1.aggregate(Max('bpub_date'))
    # list=BookInfo.books1.filter(bread__gt=20)
    # list = BookInfo.books1.filter(bread__gt=F('bcoment'))
    # list=BookInfo.books1.filter(pk__lt=4,btitle__contains='1')
    # 等价于：
    # list=BookInfo.books1.filter(pk__lt=4).filter(btitle__contains='1')
    list=BookInfo.books1.filter(Q(pk__lt=4)|Q(btitle__contains='1'))
    context = {'list1': list
               #,'Max1':Max1
               }
    return render(request, 'booktest/index_1.html', context)