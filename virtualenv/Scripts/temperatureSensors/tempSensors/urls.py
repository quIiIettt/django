from . import views 
from django.urls import path, include
from rest_framework import routers
from tempSensors.views import temperatureSensorsViewSet

router = routers.DefaultRouter()
router.register(r'temperatureSensors', temperatureSensorsViewSet)

urlpatterns = [
    path('', views.index, name = 'temperatureSensors_home'),
    path('route/', include(router.urls)),
    path('sensors/<int:id>', views.sensor_page),
]
