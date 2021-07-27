# -*- coding=utf-8 -*-
# @Time : 2021/7/27 19:48
# @Author : YonglaiZhao
# @File: urls.py.py
# @Software: PyCharm

from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
