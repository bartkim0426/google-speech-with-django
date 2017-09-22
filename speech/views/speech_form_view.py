from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from ..forms import SpeechForm


class SpeechFormView(LoginRequiredMixin, FormView):
    login_url = '/accounts/login/'
    form_class = SpeechForm
    template_name = "speech/convert.html"

    def form_valid(self, form):
        form.save()
        # from IPython import embed; embed()
        return super(SpeechFormView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SpeechFormView, self).get_context_data(**kwargs)
        context['title'] = 'CONVERT'
        return context
