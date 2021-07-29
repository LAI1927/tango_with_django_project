# -*- coding=utf-8 -*-
# @Time : 2021/7/29 14:14
# @Author : YonglaiZhao
# @File: rango_template_tags.py.py
# @Software: PyCharm

from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/categories.html')
def get_category_list(current_category=None):
    return {'categories': Category.objects.all(),
            'current_category': current_category}
