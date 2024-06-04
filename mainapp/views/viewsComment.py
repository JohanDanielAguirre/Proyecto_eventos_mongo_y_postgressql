from bson import ObjectId
from django.shortcuts import render, redirect
from django.views import View
from mainapp.forms import CommentForm
from pymongo import MongoClient
from django.conf import settings

# Create your views here.


class CommentView(View):
    form_class = CommentForm
    initial = {}
    template_name = "addComent.html"

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
            collection_name = dbname["comments"]
            # Crear documento
            event_comment = {
                "text": solicitud.get('comentario'),
                # Añade el ID del evento al comentario
                "event_id": solicitud.get('event_id'),
            }
            collection_name.insert_one(event_comment)

            return redirect("lugar_evento")

        return render(request, self.template_name, {"form": form})
