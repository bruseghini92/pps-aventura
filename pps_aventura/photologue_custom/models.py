from django.db import models
from aventuras.models import Evento
from photologue.models import Gallery


class GalleryExtended(models.Model):
    # Link back to Photologue's Gallery model.
    gallery = models.OneToOneField(
        Gallery, related_name='extended', on_delete=models.CASCADE)
    event = models.ForeignKey(Evento, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'Extra fields'
        verbose_name_plural = u'Extra fields'

    def __str__(self):
        return self.gallery.title


    @staticmethod
    def nuevo(event):
        gallery = Gallery.objects.create(title=event.nombre)
        return (GalleryExtended.objects.create(gallery=gallery, event=event))
