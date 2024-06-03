from django.views import View
from django.shortcuts import render
from mainapp.models import Event


class EventsView(View):
    def get(self, request):
        eventosListados = Event.objects.all()
        return render(request, "crearEvento.html", {"eventos": eventosListados})

    def post(self, request):
        eventoId = request.POST.get('evento_id')
        evento_seleccionado = None
        if eventoId:
            evento_seleccionado = Event.objects.get(
                id=eventoId)
        eventosListados = Event.objects.all()
        return render(request, "crearEvento.html", {"eventos": eventosListados, "evento_seleccionado": evento_seleccionado})
