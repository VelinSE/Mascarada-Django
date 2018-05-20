from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth.views import login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from custom_auth.views import register, profile, logout_user


urlpatterns = [
    url(r'^register/$', register, name="register"),
    url(r'^login/$', login, { "template_name" : "login.html" } ,name='login'),
    url(r'^profile/$', profile, name = 'profile'),
    url(r'^logout/$', logout_user, name='logout'),
    url(r'^reset-password/$', password_reset, name='reset_password'),
    url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete, name='password_reset_complete'),
]