from django.views.generic import ListView, CreateView, View
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404

from ..models import Speech
from ..forms import InputFileForm


class UploadView(View):
    speeches = Speech.objects.all().order_by('created_at')

    def get(self, request):
        context_dict = {
            'speeches': self.speeches,
        }
        # from IPython import embed; embed()
        template_name = 'speech/list.html'

        return render(request, template_name, context_dict)

    def post(self, request):
        try:
            pk = request.POST.get('speech_pk')
            speech = get_object_or_404(Speech, id=pk)
        except:
            pass

        if request.FILES.get('docx_input'):
            docx_input = request.FILES.get('docx_input')

            speech.docx_input = docx_input
            speech.save()
        if request.FILES.get('docx_output'):
            docx_output = request.FILES.get('docx_output')
            speech.docx_output = docx_output
            speech.save()

        context_dict = {
            'speeches': self.speeches,
        }
        template_name = 'speech/list.html'

        return render(request, template_name, context_dict)


# class SpeechListView(ListView):
#     model = Speech
#     template_name = "speech/list.html"
#     context_object_name = "speeches"

#     def get_context_data(self, **kwargs):
#         context = super(SpeechListView, self).get_context_data(**kwargs)
#         context['title'] = 'LIST'
#         return context

# CreateView는 object 생성
# class UploadFileView(CreateView):
#     model = Speech
#     field = ['docx_input']
#     form_class = InputFileForm
#     success_url = reverse_lazy('speech:list')
#     template_name = "speech/list.html"

#     def get_context_data(self, **kwargs):
#         kwargs['speeches'] = Speech.objects.order_by('-created_at')
#         return super(UploadFileView, self).get_context_data(**kwargs)
