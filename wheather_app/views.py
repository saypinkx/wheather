from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import WheatherForm
import requests


class WheatherView(View):
    def get(self, request):
        form = WheatherForm()
        data = {'form': form}
        return render(request, 'wheather_app/wheather.html', context=data)
    def post(self, request):
        form = WheatherForm(request.POST)
        if form.is_valid():
            try:
                city = form.cleaned_data['city']
                info = self.get_info(city)
                data = {'form':form, 'main': info['main'], 'description': info['weather'], 'info': info}
                return render(request, 'wheather_app/wheather.html', context=data)
            except:
                return HttpResponse('Такого города не найдено')

    @classmethod
    def get_info(cls, city):
        appid = '1aff7250761c5eed68c1de76316c0875'
        response = requests.get("http://api.openweathermap.org/data/2.5/weather",
        params={'q': city, 'lang': 'ru', 'APPID': appid, 'units': 'metric', 'cnt': 40})
        info = response.json()
        return info
