from django.db import models
from tickets.models import Visitor
from django.core.validators import MaxValueValidator, MinValueValidator

class Camping(models.Model):
    camping_number = models.IntegerField()
    free_beds = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)])

class Spot(models.Model):
    beds_taken = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    camping = models.ForeignKey(Camping, on_delete=models.PROTECT)

class Tent(models.Model):
    taken_time = models.DateTimeField(null=True, blank=True)
    returned_time = models.DateTimeField(null=True, blank=True)
    size = models.IntegerField()

class Reservation(models.Model):
    spot = models.ForeignKey(Spot, on_delete=models.PROTECT)
    visitor = models.ForeignKey(Visitor, on_delete=models.PROTECT)
    tent = models.ForeignKey(Tent, on_delete=models.PROTECT, null=True, blank=True)

