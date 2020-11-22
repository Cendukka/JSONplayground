from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("temperatures", views.temperature, name="Temperature"),
    path("temperatures/<int:temp_id>/", views.temperature_id, name="Temperature"),
    path("winds", views.wind, name="Wind"),
    path("winds/<int:wind_id>", views.wind_id, name="Wind"),
]
