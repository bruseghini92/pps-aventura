from django.conf.urls import include, url
from django.urls import path, re_path
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    re_path(r'^eventos/', views.events, name="all-events"),
    re_path(r'^photologue/', include('photologue.urls', namespace='photologue')),
    path('radio',views.radio),
    #re_path(r'^search/$', views.search, name="search-service"),
    url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    path('all/', views.EventoListView.as_view(), name='evento-list'),
    path('<pk>/', views.EventoDetailView.as_view(), name='evento-detail'),  
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)