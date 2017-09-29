from django.conf.urls import url, include
from django.contrib.admin.views.decorators import staff_member_required

from .views import SpeechDetailView, SpeechFormView, UploadView, SpeechListView


urlpatterns = [
    url(r'^convert/$', staff_member_required(SpeechFormView.as_view(success_url="/speeches/")), name='convert'),
    url(r'^$', staff_member_required(SpeechListView.as_view()), name='list'),
    # url(r'^$', staff_member_required(UploadView.as_view()), name='list'),
    url(r'^(?P<pk>[-\w]+)/$', staff_member_required(SpeechDetailView.as_view()), name='detail'),
]
