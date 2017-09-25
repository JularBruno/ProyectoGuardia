# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import *

# Create your views here.

def index(request):
    first = guardia.objects.all()
    return render(request, "base.html", {"guardias": first})


def registro(request):
    second = guardia.objects.all()
    return render(request, "registro.html", {"guardias": second})

def salida(request):
    tercero = guardia.objects.all()
    return render(request, "salidas.html", {"guardias": tercero})

#def familia(request):
 #   cuarto = guardia.objects.all()
  #  return render(request, "familias.html", {"guardias": cuarto})


def upload(request):
    name=request.POST['nombre']
    new=guardia(nombre=name)
    new.save()
    #return render(request, "base.html", {"guardias": [new.nombre]})
    return redirect(index)
