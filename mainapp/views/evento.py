
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect

def editContract(request):
    
    return render(request,"crearEvento.html")