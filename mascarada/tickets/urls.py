from django.conf.urls import url
from tickets.views import buy_tickets, my_tickets, tickets, resend_qr, success

urlpatterns = [
    url(r'^$', tickets, name='tickets'),
    url(r'^buy-tickets/$', buy_tickets, name='buy-tickets'),
    url(r'^my-tickets/$', my_tickets, name='my-tickets'),
    url(r'^resend-ticket/$', resend_qr, name='resend-ticket'),
    url(r'^success/', success, name='success')
]