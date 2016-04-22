# -*- coding: utf-8 -*-

from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^about$', views.about),
    url(r'^demo$', views.demo),
    url(r'^compute$', views.compute),
]
