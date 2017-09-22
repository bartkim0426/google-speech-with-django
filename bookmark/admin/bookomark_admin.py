from django.contrib import admin

from ..models import Bookmark


class BookmarkAdmin(admin.ModelAdmin):
    lis_display = ('title', 'url', 'order', 'is_active', 'clicked')

admin.site.register(Bookmark, BookmarkAdmin)
