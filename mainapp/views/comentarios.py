
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect

def crearComentario(request):
    
    return render(request,"comentarios.html")