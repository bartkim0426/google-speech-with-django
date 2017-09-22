import json
import datetime

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from ..utils import get_ku_notice
from ..models import NowData


def noticerefresh(request):
    if request.method == "POST":
        now = request.POST.get('now_time')
        # from IPython import embed; embed()
        now = datetime.datetime.strptime(now, '%Y-%m-%dT%H:%M:%S.%fZ')
        get_ku_notice()
        # from IPython import embed; embed()
        # now = now.strftime("%Y년 %m월 %y일 %I:%M %p")
        if NowData.objects.count() == 0:
            NowData.objects.create(
                now=now,
            )
        else:
            nowdate = NowData.objects.first()
            nowdate.now = now
            nowdate.save()
        # from IPython import embed; embed()
        now_str = now.isoformat()
        # now = NowData.objects.first().now
        # from IPython import embed; embed()

        ctx = {'now': now_str}
    # use mimetype instead of content_type if django < 5
    return HttpResponse(json.dumps(ctx), content_type='application/json')
