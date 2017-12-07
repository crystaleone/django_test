from django.conf.urls import url
import views
urlpatterns=[

    url(r'^index_1$',views.index_1),
    url(r'^myexp$',views.myExp),
    url(r'^uploadPic$',views.uploadPic),
    url(r'^uploadHandle$',views.uploadHandle),
    url(r'^herolist/(\d+)/$',views.herolist),
    url(r'^$',views.index),
    #url(r'^area/(\d+)/$',views.area2),
    url(r'^pro/$',views.pro),
    url(r'^city(\d+)/$',views.city),
    url(r'^htmlEditor/$',views.htmlEditor),
    url(r'^htmlEditorHandle/$',views.htmlEditorHandle),
    url(r'^cache1/$',views.cache1),
    url(r'mysearch/$',views.mysearch),
    url(r'^celeryTest/$',views.celeryTest),
]