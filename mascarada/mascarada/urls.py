from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^accounts/', include('custom_auth.urls')),
    url(r'^tickets/', include('tickets.urls')),
    url(r'^camping/', include('camping.urls')),
    url(r'^admin/', admin.site.urls),
]
