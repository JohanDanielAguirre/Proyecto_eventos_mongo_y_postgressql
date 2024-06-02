from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from django.views.generic import RedirectView


def homeView(request):
    return render(request, 'home.html')

