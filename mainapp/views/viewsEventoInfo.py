# views.py
from django.views import View
from django.shortcuts import render, get_object_or_404
from pymongo import MongoClient
from django.conf import settings


class EventDetailView(View):
    def get(self, request, event_id):
        # Conectar a MongoDB
        client = MongoClient(settings.MONGO_URI)
        db = client.get_database('Proyecto_SID2')
        eventos_collection = db['events']

        # Obtener el documento específico del evento
        evento = eventos_collection.find_one({'_id': event_id})

        if not evento:
            # Manejo de evento no encontrado
            return render(request, '404.html', {})

        # Pasar los datos del evento a la plantilla
        context = {
            'titulo': evento.get('titulo', ''),
            'categorias': evento.get('categorias', []),
            'fecha': evento.get('fecha', ''),
            'lugar': evento.get('lugar', ''),
            'descripcion': evento.get('descripcion', ''),
            'programas': evento.get('programas', []),
            'facultades': evento.get('facultades', []),
            'conferencistas': evento.get('conferencistas', []),
            'asistentes': evento.get('asistentes', []),
            'comentarios': evento.get('comentarios', [])
        }

        return render(request, 'eventInform.html', context)
