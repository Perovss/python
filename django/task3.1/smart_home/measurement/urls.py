from django.urls import path
from measurement.views import Sensors, OneSensor, Measurements

urlpatterns = [
    path('sensors/', Sensors.as_view()),
    path('sensors/<int:pk>/', OneSensor.as_view()),
    path('measurements/', Measurements.as_view()),
]
