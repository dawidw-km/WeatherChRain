from weather.models import WeatherData

class TestHelpers:

    def create_record(self, city, temperature, perceived_temperature, humidity, rainfall_mm, creation_date):
        record = WeatherData(
            city=city,
            temperature=temperature,
            perceived_temperature=perceived_temperature,
            humidity=humidity,
            rainfall_mm=rainfall_mm,
        )
        record.full_clean()
        record.save()
        record.created_at = creation_date
        record.save()
        record.refresh_from_db()
        return record