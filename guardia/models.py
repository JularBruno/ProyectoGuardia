# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class guardia(models.Model):
	nombre = models.TextField()

	def __str__(self):
		return self.nombre
