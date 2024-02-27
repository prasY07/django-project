from django.urls import path
from customadmin.views.Auth import admin_login
from customadmin.views.Home import *
from customadmin.views.Admin import *
urlpatterns = [
    path('',admin_login, name="login"),
    path('dashboard',home, name="dashboard"),
    path('all-admins',list, name="all-admins"),
    path('add-admin',home, name="add-admin"),
    path('update-admin/<int>',home, name="update-admin"),
    path('delete-admin/<int>',home, name="delete-admin"),
]
