from django.shortcuts import render
from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Evento


def index(request):
    context = {'event_list': Evento.objects.all()}
    return render(request, 'aventuras/index.html', context)


def events(request):
    if 'search' in request.GET:
        query = Evento.objects.filter(
            # Q(nombre=request.GET['search']) | Q(
            # tags__name__in=request.GET['search'])
            nombre=request.GET['search']).distinct()
        context = {'event': query}
    else:
        context = {'event_list': Evento.objects.all()}
    return render(request, 'aventuras/events.html', context)

class EventoListView(ListView):

    model = Evento
    paginate_by = 10  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class EventoDetailView(DetailView):

    model = Evento

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
