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
        self.create_weather_record(
            "Poznań",
            "https://api.open-meteo.com/v1/forecast?latitude=52.4064&longitude=16.9252&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation"
            )
        self.create_weather_record(
            "Łódź",
            "https://api.open-meteo.com/v1/forecast?latitude=51.7592&longitude=19.4560&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation"
            )
        self.create_weather_record(
            "Szczecin",
            "https://api.open-meteo.com/v1/forecast?latitude=53.4285&longitude=14.5528&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation"
            )
        self.create_weather_record(
            "Lublin",
            "https://api.open-meteo.com/v1/forecast?latitude=51.2465&longitude=22.5684&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation"
            )
        self.create_weather_record(
            "Katowice",
            "https://api.open-meteo.com/v1/forecast?latitude=50.2649&longitude=19.0238&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation"
            )
        self.create_weather_record(
            "Białystok",
            "https://api.open-meteo.com/v1/forecast?latitude=53.1325&longitude=23.1688&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation"
            )
        self.create_weather_record(
            "Rzeszów",
            "https://api.open-meteo.com/v1/forecast?latitude=50.0412&longitude=21.9991&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation"
            )
        self.create_weather_record(
            "Kielce",
            "https://api.open-meteo.com/v1/forecast?latitude=50.8661&longitude=20.6286&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation"
            )
        self.create_weather_record(
            "Opole",
            "https://api.open-meteo.com/v1/forecast?latitude=50.6751&longitude=17.9213&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation"
            )
        self.create_weather_record(
            "Bydgoszcz",
            "https://api.open-meteo.com/v1/forecast?latitude=53.1235&longitude=18.0084&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation"
            )
        self.create_weather_record(
            "Gorzów Wielkopolski",
            "https://api.open-meteo.com/v1/forecast?latitude=52.7368&longitude=15.2288&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation"
            )