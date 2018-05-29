from django.db import models
#from django.contrib.gis.db import models as modelgis

# Create your models here.
class Evento(models.Model):
    nombre = models.CharField(max_length=20, blank=True, null=True)
    reglamento = models.TextField(max_length=200,blank=True, null=True)
    inscripcion = models.URLField(max_length=30,blank=True, null=True)
    resultado = models.FileField(null=True)
    foto = models.ImageField()
    videos = models.URLField(max_length=30,blank=True, null=True)
    #ScomoLlegar = modelgis.PointField()

    def __str__(self):
        return 

    def __unicode__(self):
        return 

