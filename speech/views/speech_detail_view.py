import requests
import json

from django.core.files import File
from django.views.generic import DetailView

from ..models import Speech
from ..utils import get_result
from ..utils import convert_to_docx


class SpeechDetailView(DetailView):
    model = Speech
    template_name = "speech/detail.html"

    def get_context_data(self, **kwargs):
        context = super(SpeechDetailView, self).get_context_data(**kwargs)
        doing = None
        if self.object.content:
            pass
        else:
            try:
                operation_name = self.object.operation_name
                content = get_result(operation_name)
                if type(content) != int:
                    self.object.content = content
                    self.object.convert_done = True
                    self.object.save()

                    title = self.object.lecture_date.strftime('%m-%d')
                    date = self.object.lecture_date.strftime('%Y년 %m월 %d일 %A')

                    document = convert_to_docx(title, date, content)
                    doing = content
                    file_name = title + '.docx'
                    document.save(file_name)
                    f = open(file_name, 'rb')
                    django_file = File(f)
                    self.object.docx_input.save(file_name, django_file, save=True)
                    f.close()

                else:
                    doing = "현재 {i} 퍼센트 완료되었습니다. 조금만 기다려 주세요.".format(i=content)

            except:
                doing = "operation이 만료하였거나 변환에 실패하였습니다."

        context['title'] = self.object.file_name
        context['doing'] = doing

        return context
