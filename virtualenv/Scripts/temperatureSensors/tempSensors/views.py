from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import *



def index(request):
    sensors = TemperatureSensors.objects.all()
    return render(request, 'index.html', {'sensors': sensors})

def sensor_page(request, location):
    try:
        sensor = TemperatureSensors.objects.get(location = location)
        sensor = [(str(k).capitalize().replace('_',''), v) for k, v in sensor.__dict__.items()]
    except ObjectDoesNotExist:
        return HttpResponse("wrong location")
    return render(request, 'dja3prac.html', {'server': sensor[1:]})