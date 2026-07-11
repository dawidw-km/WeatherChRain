from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class WeatherData(models.Model):
    
    city = models.CharField(max_length=100)
    temperature = models.FloatField(
        validators=[
            MinValueValidator(-80),
            MaxValueValidator(80)
        ]
    )
    perceived_temperature = models.FloatField(
        validators=[
            MinValueValidator(-80),
            MaxValueValidator(80)
        ]
    )
    humidity = models.DecimalField(
        max_digits=4, decimal_places=2,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1)
        ]
    )
    rainfall_mm = models.FloatField(
        validators=[
            MinValueValidator(0.0)
            ]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.city} temp:{self.temperature},"
            f" humidity:{self.humidity},"
            f" rainfall:{self.rainfall_mm},"
            f" time:{self.created_at}"
        )
