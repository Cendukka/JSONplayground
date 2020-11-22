import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Temperature(models.Model):
    temperature_name = models.CharField(max_length=255)
    temperature_c = models.CharField(max_length=3)
    measure_date = models.DateTimeField('date measured')

    def __str__(self):
        return self.temperature_name

    def last_three_days(self):
        return self.temperature_c

class Wind(models.Model):
    wind_name = models.CharField(max_length=255)
    wind_MperS = models.IntegerField(default=0)
    measure_date = models.DateTimeField('date measured')

    def __str__(self):
        return self.wind_name