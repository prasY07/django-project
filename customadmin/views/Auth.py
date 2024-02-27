from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.http import HttpResponse


def admin_login(request):
    return render(request,"index.html")
        