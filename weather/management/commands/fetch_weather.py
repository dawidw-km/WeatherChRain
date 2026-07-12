import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from decimal import Decimal
from weather.models import WeatherData
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Fetch weather data"

    def handle(self, *args, **options):
        url = 'https://api.open-meteo.com/v1/forecast?latitude=53.78&longitude=20.48&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation'

        retry = Retry(
            total=5,
            backoff_factor=1,
            status_forcelist=[500, 502, 503, 504],
        )
        session = requests.Session()
        session.mount('http://', HTTPAdapter(max_retries=retry))

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.RequestException:
            self.stdout.write("Error fetching data")
            return

        current_data = data["current"]
        if not current_data:
            self.stdout.write("Error fetching data")
            return

        record = WeatherData(
            city = "Olsztyn",
            temperature = current_data["temperature_2m"],
            perceived_temperature = current_data["apparent_temperature"],
            humidity = Decimal(str(round(current_data["relative_humidity_2m"] / 100, 2))),
            rainfall_mm = current_data["precipitation"]
        )
        record.full_clean()
        record.save()