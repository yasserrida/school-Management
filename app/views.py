from django.shortcuts import render
from .models import student
import environ

env = environ.Env()
environ.Env.read_env()
sidebar = [{'name': 'Dashboard', 'url': '/dashboard', 'icon': 'fa-tv'},
           {'name': 'Etudiants', 'url': '/etudiants', 'icon': 'fa-users'},
           {'name': 'Notes', 'url': '/notes', 'icon': 'fa-sticky-note'}]


def index(request):
    return render(request, 'index.html', {'APP_Name': env('APP_NAME')})


def login(request):
    return render(request, 'login.html', {'APP_Name': env('APP_NAME')})


def dashboard(request):
    return render(request, 'pages/dashboard.html', {'APP_Name': env('APP_NAME'), 'side_bar_items': sidebar})


def users(request):
    return render(request, 'pages/users.html', {'APP_Name': env('APP_NAME'), 'side_bar_items': sidebar})
