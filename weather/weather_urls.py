from django.urls import path
from .views import CityWeatherListView

urlpatterns = [
    path(
        "weather/<str:city>/",
        CityWeatherListView.as_view(),
        name="city-weather"
    ),
]