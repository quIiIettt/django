from django.db import models
import datetime


class TemperatureSensors(models.Model):
    location = models.CharField('Location of the sensor',
        max_length = 255, blank = False)
    dateMeasurement = models.DateField('Date of temperature measurement',
        default = datetime.date.today, blank = False)
    timeMeasurement = models.DateField('Time of temperature measurement',
        default = datetime.time, blank = False)
    temperature = models.IntegerField('Temperature',
        default = 0, blank = False)
    name = models.CharField('Sensor name',
        max_length = 50, blank = False)
    model = models.CharField('Sensor model',
        max_length = 50, blank = False)
    group = models.CharField('The group to which the sensor belongs',
        max_length = 50, blank = False)