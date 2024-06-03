from django.views import View
from django.shortcuts import redirect, render
from django.conf import settings
from pymongo import MongoClient
from bson import ObjectId


class EventDetailView(View):
    def get(self, request, event_id):
        # Conectar a MongoDB
        client = MongoClient(settings.MONGO_URI)
        db = client.get_database('Proyecto_SID2')
        eventos_collection = db['events']

        # Obtener el documento del evento usando ObjectId
        evento = eventos_collection.find_one({'_id': ObjectId(event_id)})
        if evento:
            evento['id'] = str(evento['_id'])
            # Eliminar el campo _id para evitar el error de plantilla
            del evento['_id']
            print(evento.get('descripcion', ''))
            # Pasar los campos del evento como contexto a la plantilla
            return render(request, 'informEvent.html', {
                'titulo': evento.get('title', ''),
                'categorias': evento.get('categories', []),
                'fecha': evento.get('date', ''),
                'lugar': evento.get('lugar', ''),
                'descripcion': evento.get('description', ''),
                'programas': evento.get('programs', []),
                'facultades': evento.get('facultades', []),
                'conferencistas': evento.get('conferencistas', []),
                'asistentes': evento.get('asistentes', []),
                'comentarios': evento.get('comments', []),
            })

        # Manejo del caso en que el evento no se encuentre
        # Puedes agregar aquí una redirección o un mensaje de error
