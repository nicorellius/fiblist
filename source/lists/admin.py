"""
file        :   admin.py (lists)
date        :   2016-03-31
description :   admin for lists app
"""


from django.contrib import admin

from lists.models import List, Item


class ListAdmin(admin.ModelAdmin):
    pass
    # list_filter = ['created', ]
    # date_hierarchy = 'created'
    # save_on_top = True


class ItemAdmin(admin.ModelAdmin):

    list_display = ['text', 'list', ]
    # list_filter = ['created', ]
    # search_fields = ['list', '', ]
    # date_hierarchy = 'created'
    # save_on_top = True
    #
    # fieldsets = (
    #     (None, {
    #         'fields': ('text', 'list',)
    #     }),
    # )

admin.site.register(List, ListAdmin)
admin.site.register(Item, ItemAdmin)
