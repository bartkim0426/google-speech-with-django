from django.conf.urls import url, include

from .views import NoticeListView, noticeimportant, noticerefresh

urlpatterns = [
    url(r'^$', NoticeListView.as_view(), name='list'),
    url(r'^important/$', noticeimportant, name='important'),
    url(r'^refresh/$', noticerefresh, name='refresh'),
]
