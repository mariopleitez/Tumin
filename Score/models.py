# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class VariableTipo(models.Model):
    Nombre = models.CharField(max_length=200, null=True, unique=True)
    Descripcion = models.CharField(max_length=500, null=True, unique=True)
    
    Enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Nombre

class VariableNombre(models.Model):
    Tipo = models.ForeignKey(VariableTipo, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=200, null=True, unique=True)
    Descripcion = models.CharField(max_length=500, null=True, unique=True)

    Enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.Tipo) + ' / ' + self.Nombre

class VariableValor(models.Model):
    Nombre = models.ForeignKey(VariableNombre, on_delete=models.CASCADE)
    Valor = models.CharField(max_length=200, null=True, unique=False)
    Puntaje = models.IntegerField(default=0)

    Enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.Nombre) + ': ' + str(self.Valor)

    class Meta:
        unique_together = ('Nombre', 'Valor', 'Puntaje')


class Riesgo(models.Model):
    Riesgo = models.CharField(max_length=200, null=True, unique=True)
    Nombre = models.CharField(max_length=200, null=True, unique=True)
    Descripcion = models.CharField(max_length=500, null=True)
    PuntajeMinimo = models.IntegerField(default=0)
    PuntajeMaximo = models.IntegerField(default=0)
    
    Enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Nombre