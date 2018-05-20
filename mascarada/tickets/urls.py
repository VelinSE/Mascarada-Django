from django.conf.urls import url
from tickets.views import buy_tickets, my_tickets, sad, sadd

urlpatterns = [
    url(r'^buy-tickets/$', buy_tickets, name='buy-tickets'),
    url(r'^my-tickets/$', my_tickets, name='my-tickets'),
    url(r'^test/$', sadd)
]