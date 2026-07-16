from django.urls import path
from .views import (
    CityWeatherListView,
    CitiesListView
    )

urlpatterns = [
    path(
        "weather/<str:city>/",
        CityWeatherListView.as_view(),
        name="city-weather"
    ),
    path(
        "cities/",
        CitiesListView.as_view(),
    )
]