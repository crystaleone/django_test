# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *
# Create your views here.
from django.http import HttpResponse

def index(request):
    # hero=HeroInfo.objects.get(pk=1)
    # context={'hero':hero}
    list=HeroInfo.objects.filter(isDelete=False)
    context={'List':list}
    return render(request,'booktest/index_1.html',context)
def show(request, id,id2):
    context={'id':id}
    return render(request, 'booktest/show.html',context)

def index2(request):
    return render(request,'booktest/index2.html')
def user1(request):
    context={'uname':'xizong'}
    return render(request,'booktest/user1.html',context)
def user2(request):
    return render(request, 'booktest/user2.html')

def htmlTest(request):
    context={'t1':'<h1>123</h1>'}
    return render(request, 'booktest/htmlTest.html',context)

def csrf1(request):
    return render(request,'booktest/csrf1.html')
def csrf2(request):
    uname=request.POST['uname']
    return HttpResponse(uname)

def verifycode(request):
    from PIL import Image,ImageDraw,ImageFont
    import random
    bgcolor=(random.randrange(0,255),random.randrange(0,255),0)
    width=100
    height=25
    image=Image.new('RGB',(width,height),bgcolor)
    font=ImageFont.truetype('FreeMono.ttf',24)
    draw=ImageDraw.Draw(image)
    text='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz'
    texttemp=''
    for i in range(4):
        texttemp1=text[random.randrange(0,len(text))]
        texttemp+=texttemp1
        draw.text((i*25,0),
                  texttemp1,
                  (255,255,255),
                  font)
    request.session['code']=texttemp
    import cStringIO
    buf=cStringIO.StringIO()
    image.save(buf,'png')
    return HttpResponse(buf.getvalue(),'image/png')
def verifytest1(request):
    return render(request,'booktest/verifytest1.html')
def verifytest2(request):
    code1=request.POST['code1']
    code2=request.session['code']
    if code1==code2:
        return HttpResponse("ok")
    else:
        return HttpResponse("no")