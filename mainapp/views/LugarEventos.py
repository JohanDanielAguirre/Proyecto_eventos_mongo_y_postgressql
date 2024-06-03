from django.shortcuts import render, redirect
from django.views import View
from mainapp.forms import LugarEventoForm
from pymongo import MongoClient
from django.conf import settings

class LugarEventoView(View):
    form_class = LugarEventoForm
    initial = {}
    template_name = "lugar_evento_form.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            solicitud = form.cleaned_data

            # Conectar a MongoDB
            my_client = MongoClient(settings.MONGO_URI)
            dbname = my_client.get_database('Proyecto_SID2')
            collection_name = dbname["lugares_eventos"]

            # Crear documento
            lugar_evento = {
                "nombre": solicitud.get('nombre'),
                "direccion": solicitud.get('direccion'),
                "ciudad": solicitud.get('ciudad'),
            }
            collection_name.insert_one(lugar_evento)

            return redirect("lugar_evento")

        return render(request, self.template_name, {"form": form})
