import inspect
from django.contrib import admin
from django.conf import settings


class SortableTabularInline(admin.TabularInline):
    template = u'admin/tabular.html'
    ng_sortable_class_name = u'ng-sortable-inline'
    ng_sortable_color_selected = u'#90EE90'
    ng_sortable_color_new = u'#FFD700'
    ng_sortable_field_name = u'position'
    ng_sortable_field_multiplier = 1

    class Media:
        js = (
            u'%sjs/jquery-1.9.1.js' % settings.STATIC_URL,
            u'%sjs/jquery-ui-1.10.3.custom.min.js' % settings.STATIC_URL,
        )

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(SortableTabularInline, self).get_formset(request, obj, **kwargs)
        for att, value in [(k, v) for k,v in inspect.getmembers(self.__class__) if k.startswith(u'ng_sortable')]:
            setattr(formset, att, value)
        return formset
