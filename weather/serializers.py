from rest_framework import serializers
from .models import WeatherData


class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = [
            "city",
            "temperature",
            "perceived_temperature",
            "humidity",
            "rainfall_mm",
            "created_at"
        ]
        read_only_fields = fields

class CitiesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = ["city"]
        read_only_fields = fields