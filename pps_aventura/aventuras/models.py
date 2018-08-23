from django.db import models
#from django.contrib.gis.db import models as modelgis

# Create your models here.


class Evento(models.Model):
    nombre = models.CharField(max_length=30, blank=True, null=True)
    reglamento = models.TextField(max_length=200, blank=True, null=True)
    inscripcion = models.URLField(max_length=30, blank=True, null=True)
    resultado = models.FileField(blank=True, null=True)
    foto = models.ImageField(blank=True, null=True)
    videos = models.URLField(max_length=30, blank=True, null=True)
    recorrido = models.URLField(blank=True, null=True, default="https://www.google.com/maps/d/u/0/")
    fecha = models.DateField()
    ourEvent = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre
