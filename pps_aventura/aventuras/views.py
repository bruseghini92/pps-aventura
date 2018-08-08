from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Evento
from photologue.models import Gallery, Photo
from .form import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def index(request):
    context = {'event_list': Evento.objects.all(),
               'slide_list': Photo.objects.filter(galleries=Gallery.objects.get(title='slide'))}
    # 'photo_list':Photo.objects.filter(gallery="tuvieja")}
    return render(request, 'aventuras/index.html', context)


def radio(request):
    return render(request, 'aventuras/radio.html')


def about_us(request):
    return render(request, 'aventuras/about_us.html')


def contact_us(request):
    return render(request, 'aventuras/contact_us.html')


def sentMessage(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            evento = form.cleaned_data['evento']
            message = form.cleaned_data['message']
            complete_text = 'Nombre:'+name+'\n Teléfono celular:'+phone+'\n Mensaje:'+message
            try:
                send_mail(evento, 
                        complete_text, 
                        email, 
                        ['aventurasdeportivassrl@gmail.com'],
                        fail_silently=False,
                        )
            except BadHeaderError:
                return HttpResponse('Algo estuvo mal por aquí')
            return redirect('success')
    return render(request, "aventuras/contact_us.html", {'form': form})


def successView(request):
    return render(request, 'aventuras/success.html')


def events(request):
    if 'search' in request.GET:
        query = Evento.objects.filter(
            # Q(nombre=request.GET['search']) | Q(
            # tags__name__in=request.GET['search'])
            nombre=request.GET['search']).distinct()
        context = {'event': query}
    else:
        context = {'event_list': Evento.objects.filter(ourEvent=True)}
    return render(request, 'aventuras/events.html', context)


class EventoListView(ListView):

    model = Evento
    paginate_by = 10  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = {'object_list': Evento.objects.filter(ourEvent=True)}
        return context


class EventoDetailView(DetailView):

    model = Evento

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
