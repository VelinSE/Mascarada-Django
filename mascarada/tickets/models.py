from django.db import models
from custom_auth.models import CustomUser


class Visitor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    rfid_code = models.CharField(max_length=10)
    birth_date = models.DateField()
    event_money = models.DecimalField(decimal_places=2, max_digits=10)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)

class EntryTicket(models.Model):
    qr_code = models.CharField(max_length=50)
    entry_date = models.DateTimeField()
    exit_date = models.DateTimeField()
    visitor = models.ForeignKey(Visitor, on_delete=models.PROTECT)