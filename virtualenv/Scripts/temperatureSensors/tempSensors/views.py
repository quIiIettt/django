from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import *



def index(request):
    sensors = temperatureSensors.objects.all()
    return render(request, 'tempSensors/index.html', {'sensors': sensors})

def sensor_page(request, id):
    try:
        sensor = temperatureSensors.objects.get(id = id)
        sensor = [(str(k).capitalize().replace('_',''), v) for k, v in sensor.__dict__.items()]
    except ObjectDoesNotExist:
        return HttpResponse("wrong id")
    return render(request, 'tempSensors/tempSensors.html', {'server': sensor[1:]})