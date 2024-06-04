from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from pymongo import MongoClient
from bson import ObjectId

from mainapp.forms import UserForm


class UserDetail(View):
    template_name = 'userInformation.html'
    
    def get(self, request, *args, **kwargs):
        user_id = self.kwargs.get("id")  # Obtén el valor del parámetro "id"
        client = MongoClient(settings.MONGO_URI)
        db = client.get_database('Proyecto_SID2')
        collection = db['users']
        user = collection.find_one({"_id": user_id})  # Busca el usuario por su _id
        client.close()
        if user:
            # Renderiza la información del usuario en tu plantilla HTML
            return render(request, self.template_name, {"user": user})
        else:
            return HttpResponse("Usuario no encontrado")
        
class UserForm(View):
    form_class = UserForm
    initial = {"key": "value"}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, "userForm.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            solicitud = form.cleaned_data
            # <process form cleaned data>
            client = MongoClient(settings.MONGO_URI)

            # First define the database name
            dbname = client.get_database('Proyecto_SID2')

            # Now get/create collection name
            collection = dbname["users"]
            cities_collection = dbname["cities"]
            ciudad_id = solicitud.get('ciudad')
            ciudad_info = cities_collection.find_one({"_id": ObjectId(ciudad_id)})
            user = {
                "id": solicitud.get('id'),
                "userName": solicitud.get('nombreUsuario'),
                "completedName": solicitud.get('nombreCompleto'),
                "relationship": solicitud.get('tipoRelacion'),
                "email": solicitud.get('email'),
                "ciudad": ciudad_info,
            }
            collection.insert_one(user)
            client.close()
            return redirect("evento")

        return render(request, "userForm.html", {"form": form})