# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, SensorSerializer, MeasurementSerializer

class Sensors(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class Measurements(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class SingleSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer