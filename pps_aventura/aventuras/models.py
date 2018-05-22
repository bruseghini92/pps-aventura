from django.db import models
from django.utils import timezone

class Aventuras (models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fechaInicio = models.DateTimeField()
    fechaInscripcion = models.DateTimeField()