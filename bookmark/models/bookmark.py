from django.db import models

from speech.models import TimeStampedModel


class BookmarkManager(models.Manager):
    def active(self):
        return self.filter(
            is_active=True,
        )


class Bookmark(TimeStampedModel):
    title = models.CharField(
        verbose_name="제목",
        max_length=50,
    )
    url = models.URLField()
    order = models.IntegerField(
        verbose_name="순번",
        help_text="순번대로 위에서부터 배치됩니다. 중복되면 먼저 만들어진 순서대로, 적지 않으면 가장 마지막에 나옵니다.",
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        verbose_name="활성화",
        help_text="체크를 해제하면 화면에 나타나지 않습니다.",
        default=True,
    )
    clicked = models.PositiveIntegerField(
        verbose_name="클릭수",
        default=0,
    )
    icon = models.CharField(
        verbose_name="아이콘이름",
        help_text="material icon 이름(https://material.io/icons/ 참고)을 입력해주세요 ex)face",
        max_length=20,
        default="explore"
    )
    hover = models.CharField(
        verbose_name="도움말",
        help_text="홈페이지에서 해당 링크에 마우스를 올렸을 때 나오는 도움말입니다. 아이디/비밀번호 등 원하는 정보를 적어주세요.",
        max_length=255,
        null=True,
        blank=True,
    )

    objects = BookmarkManager()

    class Meta:
        verbose_name = '북마크'
        verbose_name_plural = '북마크 관리'
        ordering = ['order']

    def __str__(self):
        return self.title
