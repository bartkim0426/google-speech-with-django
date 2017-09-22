import json
import requests
import datetime
from dateutil import parser
from bs4 import BeautifulSoup

from ..models import Notice


def get_ku_notice():
    url = "http://biz.korea.ac.kr/ko/notice?field_program_type_tid=3"

    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    col_li = soup.select(".views-column")
    notice_nids = [i.nid for i in Notice.objects.all()]

    for col in col_li:
        nid = col.select_one(".view-nid").get_text()[2:]

        if int(nid) in notice_nids:
            notice = Notice.objects.get(nid=nid)

            now = datetime.date.today()
            sub_timedelta = (now - notice.date).days

            if sub_timedelta > 7:
                notice.is_new = False
                notice.save()
            else:
                notice.is_new = True
                notice.save()
        else:
            title = col.select_one(".view-title").get_text()
            body = col.select_one(".view-body").get_text()
            date = col.select_one(".view-date").get_text()
            dt = parser.parse(date).date()
            link = col.select_one("a")
            detail_url = 'http://biz.korea.ac.kr' + link.get_attribute_list('href')[0]

            Notice.objects.create(
                title=title,
                body=body,
                date=dt,
                detail_url=detail_url,
            )
