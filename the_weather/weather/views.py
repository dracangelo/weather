from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

# Create your views here.

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=83c15dfafdd652afa05c27459ed7b1f1'
    city = 'Nairobi'

    if request.method == 'POST':
        pass

    form = CityForm()

    cities = City.objects.all()
    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city':city.name ,
            'temparature':r['main']['temp'] ,
            'description': r['weather'][0]['description'],  
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data':weather_data, 'form':form}

    return render(request, 'weather/weather.html', context)