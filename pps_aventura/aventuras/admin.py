from django.contrib import admin
#from django.contrib.gis.db import models as modelgis
from django.db import models
from photologue_custom.models import GalleryExtended
from .models import Evento

#from mapwidgets.widgets import GooglePointFieldWidget


admin.site.register(Evento)
