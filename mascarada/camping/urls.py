from django.conf.urls import url
from camping.views import reserve

urlpatterns = [
    url(r'^reserve/$', reserve, name='reserve'),
]