from django.db import models

from speech.models import TimeStampedModel


class NoticeManager(models.Manager):
    def active(self):
        return self.filter(
            is_active=True,
        )

    def new(self):
        return self.filter(
            is_new=True,
        )


class Notice(TimeStampedModel):
    nid = models.IntegerField(
        verbose_name="공지번호",
        unique=True,
    )
    title = models.CharField(
        verbose_name="공지제목",
        max_length=255,
    )
    body = models.TextField(
        verbose_name="내용요약",
    )
    date = models.DateField(
        verbose_name="공지날짜",
    )
    detail_url = models.TextField(
        verbose_name="상세페이지",
    )
    is_new = models.BooleanField(
        verbose_name="새로운 공지",
        default=True,
    )
    is_active = models.BooleanField(
        verbose_name="활성화",
        default=True,
    )
    is_important = models.BooleanField(
        verbose_name="중요",
        default=False,
    )

    objects = NoticeManager()

    class Meta:
        verbose_name = '경영대학원 공지'
        verbose_name_plural = '경영대학원 공지 관리'
        ordering = ['-date']

    def __str__(self):
        return self.title
