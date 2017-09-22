from django.contrib import admin

from ..models import WeatherLocation


class WeatherLocationAdmin(admin.ModelAdmin):
    list_display = (
        'location',
        'lat',
        'lon',
        'order',
        'is_active',
    )

admin.site.register(WeatherLocation, WeatherLocationAdmin)
