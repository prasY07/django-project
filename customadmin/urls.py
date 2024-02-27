from django.urls import path
from customadmin.views.Auth import admin_login
from customadmin.views.Home import *
urlpatterns = [
    path('',admin_login, name="login"),
    path('dashboard',home, name="dashboard"),
]
