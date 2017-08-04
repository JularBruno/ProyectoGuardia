# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import *

# Create your views here.

def index(request):
	first = guardia.objects.all()
	return render(request, "base.html", {"guardias": first})

def upload(request):
	name=request.POST['nombre']
	new=guardia(nombre=name)
	new.save()
	#return render(request, "base.html", {"guardias": [new.nombre]})
	return redirect(index)
