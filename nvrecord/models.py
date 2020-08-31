from django.db import models
from django.conf import settings
from django.utils import timezone

class Vehicle(models.Model):

    plate = models.CharField(max_length=35,unique=True)

    def __str__(self):
        return self.plate
        
class NavigationRecord(models.Model):

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now, editable=False)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return str(self.vehicle)

