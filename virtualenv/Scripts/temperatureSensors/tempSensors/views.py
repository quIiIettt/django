from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import DetailView
from rest_framework import viewsets
from tempSensors.serializers import temperatureSensorsSerializer
from tempSensors.models import temperatureSensors
from .models import *


def index(request):
    sensors = temperatureSensors.objects.all()
    return render(request, 'tempSensors/index.html', {'sensors': sensors})

def sensor_page(request, id):
    try:
        sensor = temperatureSensors.objects.get(id = id)
        sensor = [(str(k).capitalize().replace('_',''), v) for k, v in sensor.__dict__.items()]
    except ObjectDoesNotExist:
        return HttpResponse()
    return render(request, 'tempSensors/tempSensors.html', {'server': sensor[2:]})

class temperatureSensorsViewSet(viewsets.ModelViewSet):
    queryset = temperatureSensors.objects.all()
    serializer_class = temperatureSensorsSerializer