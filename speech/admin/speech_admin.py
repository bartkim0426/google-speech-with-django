from django.contrib import admin

from ..models import Speech


class SpeechAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'operation_name', 'lecture_date', 'memo', 'docx_input', 'docx_output', 'convert_done', 'transcribe_done')

admin.site.register(Speech, SpeechAdmin)
