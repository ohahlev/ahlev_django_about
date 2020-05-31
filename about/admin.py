from django.utils.html import format_html
from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.db import models
from .models import About

class AboutAdmin(admin.ModelAdmin):

    search_fields = ['whatweare', 'whatwedo', 'whoweare']

    list_display = [ 'id', 'date_created', 'last_updated',
    'preview_whatweare', 'preview_whatwedo', 'preview_whoweare' ]

    fieldsets = [
        (None, {
            'fields': ['whatweare', 'whatwedo', 'whoweare'],
        }),
    ]

    def preview_whatweare(self, obj):
        return format_html(obj.whatweare)
    preview_whatweare.admin_order_field = 'whatweare'
    preview_whatweare.short_description = 'what we are'

    def preview_whatwedo(self, obj):
        return format_html(obj.whatwedo)
    preview_whatwedo.admin_order_field = 'whatwedo'
    preview_whatwedo.short_description = 'what we do'

    def preview_whoweare(self, obj):
        return format_html(obj.whoweare)
    preview_whoweare.admin_order_field = 'whoweare'
    preview_whoweare.short_description = 'who we are'

    readonly_fields = ['preview_whatweare', 'preview_whatwedo', 'preview_whoweare']

admin.site.register(About, AboutAdmin)
