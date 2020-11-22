from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Temperature, Wind

def index(request):
    
    return HttpResponse("Hello World!")

def temperature(request):
    latest_temperatures = Temperature.objects.order_by('measure_date')[:2]
    context = {
        'latest_temperatures': latest_temperatures,
    }
    return render(request, 'weather/temperature.html')
def temperature_id(request, temp_id):
    return HttpResponse("Temperature id: %s" % temp_id)

def wind(request):
    return HttpResponse("Wind")
def wind_id(request):
    return HttpResponse("Wind")
# Create your views here.
