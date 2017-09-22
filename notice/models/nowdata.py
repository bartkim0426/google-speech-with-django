from django.db import models


class NowData(models.Model):
    now = models.DateTimeField()
