from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# from jsonfield import JSONField

from .timestamped import TimeStampedModel
from ..utils import call_transcribe_request


class Speech(TimeStampedModel):
    # api_data = JSONField()
    lecture_date = models.DateField(
        verbose_name="날짜",
    )
    content = models.TextField(
        verbose_name="수정전내용",
        null=True,
        blank=True,
    )
    content_done = models.TextField(
        verbose_name="수정완료내용",
        null=True,
        blank=True,
    )
    audio_url = models.CharField(
        max_length=128,
        verbose_name="음성파일 URL",
        help_text="'gs://cloud-storage-name/filename' 형식으로 적어주세요 ex) 'gs://speech-seul/file.flac'",
        null=True,
        blank=True,
    )
    file_name = models.CharField(
        max_length=50,
        verbose_name="파일제목",
        help_text="파일 제목은 google-cloud-storage에 올린 파일의 '.mp3', '.flac'을 제외한 파일명만 적어주세요! ex) '0906.mp3' 의 경우 '0906'",
    )
    memo = models.CharField(
        verbose_name="메모",
        max_length=128,
        null=True,
        blank=True,
    )
    operation_name = models.CharField(
        max_length=30,
        verbose_name="operation-name",
        help_text="google speech api를 호출할 때 사용하는 작업 번호입니다. 'GET https://speech.googleapis.com/v1/operations/YOUR_OPERATION_NAME?key=YOUR_API_KEY'의 YOUR_OPERATION_NAME에 넣어 주면 됩니다.",
        null=True,
        blank=True,
    )
    convert_done = models.BooleanField(
        verbose_name="변환완료",
        default=False,
    )
    transcribe_done = models.BooleanField(
        verbose_name="수정완료",
        default=False,
    )
    docx_input = models.FileField(
        verbose_name="수정전파일",
        null=True,
        blank=True,
    )
    docx_output = models.FileField(
        verbose_name="수정후파일",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = '대본'
        verbose_name_plural = '대본 관리'

    def __str__(self):
        return self.file_name

    # def save(self, force_insert=False, force_update=False, *args, **kwargs):
    #     if self.docx_output != '':
    #         self.docx_output

    #     super(Person, self).save(force_insert, force_update, *args, **kwargs)
    # def save(self, *args, **kwargs):
    #     is_new = True if not self.id else False
    #     super(Speech, self).save(*args, **kwargs)

    #     if is_new:
    #         operation_name = call_transcribe_request(self.file_name)
    #         self.operation_name = operation_name
    #         self.save()


@receiver(post_save, sender=Speech)
def post_save_speech(sender, instance, created, **kwargs):
    if created:
        post_save.disconnect(post_save_speech, sender=sender)
        operation_name = call_transcribe_request(instance.file_name)
        instance.operation_name = operation_name
        instance.save()
    try:
        if instance.docx_output.name != '':
            post_save.disconnect(post_save_speech, sender=sender)
            from docx import Document
            document = Document(instance.docx_output.path)
            content_done = ''
            for para in document.paragraphs:
                content_done += para.text
            instance.content_done = content_done
            instance.transcribe_done = True
            instance.save()
    except:
        pass
