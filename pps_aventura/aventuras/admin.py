from django.contrib import admin
#from django.contrib.gis.db import models as modelgis
from django.db import models
from .models import Evento

#from mapwidgets.widgets import GooglePointFieldWidget

# Register your models here.

admin.site.register(Evento)

"""
class CityAdmin(admin.ModelAdmin):
    formfield_overrides = {
        modelgis.PointField: {"widget": GooglePointFieldWidget}
    }
"""