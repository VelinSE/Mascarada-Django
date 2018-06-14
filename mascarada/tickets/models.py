from custom_auth.models import CustomUser
from tickets.utils import render_to_pdf

from django.db.models.signals import post_save
from django.db import models
from django.core.mail import EmailMessage
from django.dispatch import receiver
from django.http import HttpResponse

import random


class Visitor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    rfid_code = models.CharField(max_length=10, unique=True)
    birth_date = models.DateField()
    event_money = models.DecimalField(decimal_places=2, max_digits=10)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)

class EntryTicket(models.Model):
    qr_code = models.CharField(max_length=50)
    entry_date = models.DateTimeField(null=True, blank=True)
    exit_date = models.DateTimeField(null=True, blank=True)
    visitor = models.ForeignKey(Visitor, on_delete=models.PROTECT)

@receiver(post_save, sender=Visitor)
def createEntryTicket(sender, **kwargs):
    if kwargs.get('created', False):
        visitor = kwargs['instance']
        ticket = EntryTicket.objects.create(visitor=visitor)
        ticket.qr_code = generate_qr(20)
        ticket.save()

        args = { 'text' : ticket.qr_code, 'visitor' : visitor }
        pdf = render_to_pdf('purchase_email.html', args)
        response = HttpResponse(pdf, content_type='application/pdf')

        msg = EmailMessage('Mascarada', 'Welcome to mascarada!', to=[ticket.visitor.email])
        msg.attach('ticket.pdf', response.content , 'application/pdf')
        msg.send()
        

def generate_qr(len):
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*1234567890"

    value = ''.join(random.choice(symbols) for _ in range(len))
    while EntryTicket.objects.filter(qr_code=value):
        value = ''.join(random.choice(symbols) for _ in range(len))

    return value