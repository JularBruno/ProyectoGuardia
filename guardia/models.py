# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models

# Create your models here.

class Ingreso (models.Model):
	id_Ingreso = models.IntegerField(primary_key = True)
	datetime = models.DateTimeField(auto_now=True)
	
class Visitante (models.Model):
	id_Visitante = models.IntegerField(primary_key = True)
	nombre_apellido = models.CharField(max_length = 30)
	dni = models.CharField(max_length = 8)
	id_Visita = models.ForeignKey(settings.AUTH_USER_MODEL)
	id_Auto = models.ForeignKey(settings.AUTH_USER_MODEL)

class Propietario (models.Model):
	id_Propietario = models.IntegerField(primary_key = True)
	familia = models.CharField(max_length = 20)
	direccion = models.CharField(max_length = 4)
	
class Vehiculo (models.Model):
	id_Auto = models.IntegerField(primary_key = True)
	modelo = models.CharField(max_length = 30)
	patente = models.CharField(max_length = 7)
	seguro = models.charfield(max_length = 60)

class Visita (models.Model):
	id_Visita = models.IntegerField(primary_key = True)
	motivo = models.Charfield(max_length = 20)