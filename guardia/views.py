# -*- coding: utf-8 -*-
from __future__ import unicode_literals



from .models import *

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import AnonymousUser
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from datetime import datetime, timedelta
from django.utils import timezone

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



def loginv(request):
    if request.method != "POST":
        return redirect('index')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user != None:
        login(request, user)
        return redirect('index')

def logoutv(request):
    logout(request)
    cuarto = guardia.objects.all()
    return render(request, "log-in.html", {"guardias": cuarto})
