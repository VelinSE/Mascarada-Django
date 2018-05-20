from django.db import models
from custom_auth.models import CustomUser

class Camping(models.Model):
    camping_number = models.IntegerField()
    free_beds = models.IntegerField()

class Spot(models.Model):
    beds_taken = models.IntegerField()
    camping = models.ForeignKey(Camping, on_delete=models.PROTECT)

class Tent(models.Model):
    taken_time = models.DateTimeField()
    returned_time = models.DateTimeField()
    size = models.IntegerField()

class Reservation(models.Model):
    spot = models.ForeignKey(Spot, on_delete=models.PROTECT)
    visitor = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    tent = models.ForeignKey(Tent, on_delete=models.PROTECT)

