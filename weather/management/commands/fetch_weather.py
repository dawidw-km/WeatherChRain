import requests
from weather.models import WeatherData
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Fetch weather data"

    def handle(self, *args, **options):
        url = 'https://api.open-meteo.com/v1/forecast?latitude=53.78&longitude=20.48&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation'
        data = requests.get(url).json()
        current_data = data["current"]

        record = WeatherData.objects.create(
            city = "Olsztyn",
            temperature = current_data["temperature_2m"],
            perceived_temperature = current_data["apparent_temperature"],
            humidity = current_data["relative_humidity_2m"] / 100,
            rainfall_mm = current_data["precipitation"]
        )
        record.save()