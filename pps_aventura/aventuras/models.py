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
    ubicacionLat = models.CharField(max_length=50, blank=True, null=True)
    ubicacionLng = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.DateField()

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre
