from rest_framework.test import APITestCase
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
from django.urls import reverse
from weather.tests.helpers import TestHelpers

class WeatherDataAPITestCase(APITestCase, TestHelpers):
    def test_get_weather_data_for_city(self):

        record = self.create_record(
            city="TestCity",
            temperature=25.0,
            perceived_temperature=27.0,
            humidity=0.5,
            rainfall_mm=2.0,
            creation_date=timezone.now() - timedelta(hours=25)
        )

        response = self.client.get(
            reverse('city-weather', kwargs={'city': record.city}),
            {},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['city'], record.city)
        self.assertEqual(response.data[0]['temperature'], record.temperature)
        self.assertEqual(response.data[0]['perceived_temperature'], record.perceived_temperature)
        self.assertEqual(response.data[0]['humidity'], str(record.humidity))
        self.assertEqual(response.data[0]['rainfall_mm'], record.rainfall_mm)

    def test_get_weather_data_for_city_no_data(self):
        response = self.client.get(
            reverse('city-weather', kwargs={'city': 'NonExistentCity'}),
            {},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

