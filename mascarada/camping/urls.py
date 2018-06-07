from django.conf.urls import url
from camping.views import reserve, seed_campings, camping

urlpatterns = [
    url(r'^reserve/$', reserve, name='reserve'),
    url(r'^seed/$', seed_campings, name='seeder'),
    url(r'^$', camping, name='camping'),
]
