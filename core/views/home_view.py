import os
import json
import requests

from django.views.generic import FormView

from weather.forms import WeatherForm
from weather.models import WeatherLocation
from bookmark.models import Bookmark


class HomeView(FormView):
    template_name = "index.html"
    form_class = WeatherForm
    # form_classes = {
    #     'weather': WeatherForm,
    # }

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = 'HOME'
        location = "고려대학교"
        # from IPython import embed; embed()
        location = self.request.GET.get('location', 1)
        location = WeatherLocation.objects.get(id=int(location))
        lat = location.lat
        lon = location.lon

        try:
            params = {"version": "1", "lat": lat, "lon": lon}
            # your_api_key에 발급받은 api key를 넣어준다
            headers = {"appKey": os.environ["SK_PLANNET_WEATHER_API_KEY"]}
            res = requests.get("http://apis.skplanetx.com/weather/current/minutely", params=params, headers=headers)
            data = res.json()
            weather = data.get('weather').get('minutely')[0]
            form = WeatherForm(data=self.request.GET)
            context['form'] = form
        except KeyError as e:
            weather = e

        bookmarks = Bookmark.objects.active()

        context = {
            'weather': weather,
            'location': location,
            'bookmarks': bookmarks,
        }
        return context
