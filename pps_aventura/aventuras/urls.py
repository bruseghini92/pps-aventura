from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^eventos/$', views.events, name="all-events"),
    url(r'^$', views.index, name="index"),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    #url(r'^search/$', views.search, name="search-service"),
]