from django.contrib import admin
from django.conf.urls import url, include

from mascarada.views import index, lineup

urlpatterns = [
    url(r'^accounts/', include('custom_auth.urls')),
    url(r'^tickets/', include('tickets.urls')),
    url(r'^camping/', include('camping.urls')),
    url(r'^$', index, name='index'),
    url(r'^lineup/', lineup, name='lineup'),
    url(r'^admin/', admin.site.urls),
]
