from django.shortcuts import render
from django.db.models import Q
from .models import Evento


def index(request):
    if 'search' in request.GET:
        query = Evento.objects.filter(
            #Q(nombre=request.GET['search']) | Q(
                #tags__name__in=request.GET['search'])
        nombre=request.GET['search']).distinct()
        context = {'event': query}
    else:
        context = {'event_list': Evento.objects.all()}
    return render(request, 'aventuras/index.html', context)

def events(request):
    if 'search' in request.GET:
        query = Evento.objects.filter(
            #Q(nombre=request.GET['search']) | Q(
                #tags__name__in=request.GET['search'])
        nombre=request.GET['search']).distinct()
        context = {'event': query}
    else:
        context = {'event_list': Evento.objects.all()}
    return render(request, 'aventuras/events.html', context)
