from rest_framework import generics
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from django.utils.dateparse import parse_date
from .serializers import WeatherDataSerializer
from . models import WeatherData

class CityWeatherListView(generics.ListAPIView):
    serializer_class = WeatherDataSerializer

    def get_queryset(self):
        date_param = self.request.query_params.get('date')
        if date_param:
            target_date = parse_date(date_param)
            if target_date is None:
                raise ValidationError("Invalid date format. Use YYYY-MM-DD.")
        else:
            target_date = timezone.localdate()


        city = self.kwargs['city']
        return WeatherData.objects.filter(
            city=city,
            created_at__date=target_date
        ).order_by('created_at')