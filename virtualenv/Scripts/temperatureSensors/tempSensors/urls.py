from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index),
    path('sensors/<int:id>', views.sensor_page),
]
