import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from decimal import Decimal
from weather.models import WeatherData
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Fetch weather data"

    def create_weather_record(self, city, city_location):
        url = city_location
        retry = Retry(
            total=5,
            backoff_factor=1,
            status_forcelist=[500, 502, 503, 504],
        )
        session = requests.Session()
        session.mount('https://', HTTPAdapter(max_retries=retry))

        try:
            response = session.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.RequestException as e:
            self.stdout.write(f"Error fetching data: {e}")
            return

        current_data = data["current"]
        if not current_data:
            self.stdout.write("Error fetching data")
            return

        record = WeatherData(
            city = city,
            temperature = current_data["temperature_2m"],
            perceived_temperature = current_data["apparent_temperature"],
            humidity = Decimal(str(round(current_data["relative_humidity_2m"] / 100, 2))),
            rainfall_mm = current_data["precipitation"]
        )
        record.full_clean()
        record.save()

    def handle(self, *args, **options):

        self.create_weather_record(
            "Olsztyn",
            'https://api.open-meteo.com/v1/forecast?latitude=53.78&longitude=20.48&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation'
            )
        self.create_weather_record(
            "Warszawa",
            'https://api.open-meteo.com/v1/forecast?latitude=52.23&longitude=21.01&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation'
            )
        self.create_weather_record(
            "Gdańsk",
            "https://api.open-meteo.com/v1/forecast?latitude=54.3520&longitude=18.6466&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation"
            )
        self.create_weather_record(
            "Kraków",
            "https://api.open-meteo.com/v1/forecast?latitude=50.0647&longitude=19.9450&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation"
            )
        self.create_weather_record(
            "Wrocław",
            "https://api.open-meteo.com/v1/forecast?latitude=51.1079&longitude=17.0385&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation"
            )