from django.db import models
from tickets.models import Visitor

# TRANSACTIONS
class ATMLog(models.Model):
    bank_account = models.CharField(max_length=50)
    start_of_period = models.DateTimeField()
    end_of_period = models.DateTimeField()
    deposit_amount = models.IntegerField()

class Deposit(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits = 10)
    atm_log = models.ForeignKey(ATMLog, on_delete=models.PROTECT)
    visitor = models.ForeignKey(Visitor, on_delete=models.PROTECT)


# SHOPS
class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits = 10)
    Type = models.CharField(max_length=30, default='Food')

class Shop(models.Model):
    name = models.CharField(max_length=50)

class Hold(models.Model):
    quantity_in_stock = models.CharField(max_length=50)
    shop = models.ForeignKey(Shop, on_delete=models.PROTECT)
    item = models.ForeignKey(Item, on_delete=models.PROTECT)

class Purchase(models.Model):
    time = models.DateTimeField()
    visitor = models.ForeignKey(Visitor, on_delete=models.PROTECT)

class Order(models.Model):
    quantity = models.IntegerField()
    hold = models.ForeignKey(Hold, on_delete=models.PROTECT)
    purchase = models.ForeignKey(Purchase, on_delete=models.PROTECT)

class RequestedItem(models.Model):
    description = models.CharField(max_length=50)
    times_requested = models.IntegerField()


# LOANING
class LoanItem(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits = 10)
    status = models.CharField(max_length=50)

class Loan(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    item = models.ForeignKey(LoanItem, on_delete=models.PROTECT)
    visitor = models.ForeignKey(Visitor, on_delete=models.PROTECT)

# ARTISTS
class Artist(models.Model):
    name = models.CharField(max_length=70)
    short_description = models.CharField(max_length=1000)
    image_loaction = models.CharField(max_length=400)