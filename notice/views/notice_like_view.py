from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from ..models import Notice


def noticeimportant(request):
    if request.method == "POST":
        pk = request.POST.get('pk', None)
        notice = get_object_or_404(Notice, id=pk)

        if notice:
            if notice.is_important:
                notice.is_important = False
                notice.save()
            else:
                notice.is_important = True
                notice.save()

    return HttpResponse()
