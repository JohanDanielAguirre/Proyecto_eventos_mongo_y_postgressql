from django.views import View
from django.shortcuts import redirect, render
from mainapp.models import Event
from mainapp.forms import EventForm
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
from django.conf import settings


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


class EventForm(View):
    form_class = EventForm
    initial = {"key": "value"}
    template_name = "form_template.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, "eventForm.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            solicitud = form.cleaned_data
            # <process form cleaned data>
            my_client = MongoClient(settings.MONGO_URI)

            # First define the database name
            dbname = my_client.get_database('Proyecto_SID2')

            # Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
            collection_name = dbname["events"]

            #let's create two documents
            event = {
                "title": solicitud.get('title'),
                "description" : solicitud.get('description'),
                "date" : solicitud.get('date'),
                "place": solicitud.get('place'),
            }
            collection_name.insert_one(event)
            return redirect("evento")

        return render(request, "eventForm.html", {"form": form})