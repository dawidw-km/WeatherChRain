from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import WeatherDataSerializer
from . models import WeatherData

class CityWeatherListView(generics.ListAPIView):
    serializer_class = WeatherDataSerializer

    def get_queryset(self):
        city = self.kwargs['city']
        return WeatherData.objects.filter(city=city).order_by('created_at')