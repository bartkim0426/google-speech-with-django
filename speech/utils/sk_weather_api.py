import os
import json
import requests

# from ..models import WeatherLocation


def get_sk_weather(location):
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
    except KeyError as e:
        return e
    # 필요 정보들
    # temperature - tc, tmax, tmin
    # sky - name
    # rain
    # humidity(습도)
    # precipitation(강수정보)
    # return weather
