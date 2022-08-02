from multiprocessing import context
import requests
from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=83c15dfafdd652afa05c27459ed7b1f1'
    city = 'Nairobi'

    r = requests.get(url.format(city)).json()

    city_weather = {
        'city':city ,
        'temparature':r['main']['temp'] ,
        'description': r['weather'][0]['description'],  
        'icon': r['weather'][0]['icon'],
    }

    context = {'city_weather':city_weather}

    return render(request, 'weather/weather.html')