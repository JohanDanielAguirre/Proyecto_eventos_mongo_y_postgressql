from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from pymongo import MongoClient


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