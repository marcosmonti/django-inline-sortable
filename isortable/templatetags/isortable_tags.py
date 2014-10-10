#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.template import Library
from django.forms.fields import BooleanField

register = Library()

@register.inclusion_tag('admin/isortable/checkbox_toggle.html')
def toggle_block(field, formset):
    show_toggle = False
    name = ''

    if isinstance(field, BooleanField):
        for _n, _f in formset.form().fields.items():
            if _f.label == field.label:
                show_toggle = True
                name = _n
                break

    return {
        'name': name,
        'show': show_toggle
    }

