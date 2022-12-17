from rest_framework import serializers
from tempSensors.models import temperatureSensors

class temperatureSensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = temperatureSensors
        fields = ('location', 'dateMeasurement', 'timeMeasurement', 'temperature', 'name', 'model', 'group', )