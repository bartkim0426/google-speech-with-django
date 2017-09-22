from django.contrib import admin

from ..models import Notice


class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_new', 'is_important')

admin.site.register(Notice, NoticeAdmin)
