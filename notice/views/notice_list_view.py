from django.views.generic import ListView

from ..models import Notice, NowData
from ..utils import get_ku_notice


class NoticeListView(ListView):
    model = Notice
    # context_object_name = 'notices'
    template_name = "notice/list.html"

    def get_context_data(self, **kwargs):
        context = super(NoticeListView, self).get_context_data(**kwargs)

        try:
            now = NowData.objects.first().now
            context['now'] = now

        except:
            pass

        return context
