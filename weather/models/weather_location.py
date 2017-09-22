from django.db import models

from speech.models import TimeStampedModel


class WeatherLocationManager(models.Manager):
    def active(self):
        return self.filter(
            is_active=True,
        )


class WeatherLocation(TimeStampedModel):
    location = models.CharField(
        verbose_name="위치",
        max_length=10,
    )
    lat = models.CharField(
        verbose_name="위도",
        max_length=10,
    )
    lon = models.CharField(
        verbose_name="경도",
        max_length=10,
    )
    is_active = models.BooleanField(
        verbose_name="활성화",
        default=True,
    )
    order = models.IntegerField(
        verbose_name="순번",
        unique=True,
        null=True,
        blank=True,
    )

    objects = WeatherLocationManager()

    class Meta:
        verbose_name = '날씨 위치'
        verbose_name_plural = '날씨 위치 관리'
        ordering = ['order']

    def __str__(self):
        return self.location
