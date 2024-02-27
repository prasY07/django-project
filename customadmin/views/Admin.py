from django.shortcuts import render
from django.http import HttpResponse


def list(request):
    return render(request,"admins/index.html")


def add(request):
    return render(request,"index.html")

def store(request):
    return render(request,"index.html")

def edit(request):
    return render(request,"index.html")


def update(request):
    return render(request,"index.html")
        
def delete(request):
    return render(request,"index.html")