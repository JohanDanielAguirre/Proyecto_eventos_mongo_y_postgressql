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
        users_collection = db['users']
        users = [{str("id"): user["_id"], str("completedName"): user["completedName"]} for user in users_collection.find()]
        if evento:
            evento['id'] = str(evento['_id'])
            # Eliminar el campo _id para evitar el error de plantilla
            del evento['_id']
            #print(evento.get('descripcion', ''))
            
            user_ids = evento.get('speakers', [])        
            speakers = [{str("nombreCompleto"): user["completedName"], str("relacion"): user["relationship"]} for user in users_collection.find({'_id': {'$in': [ObjectId(id) for id in user_ids]}})]
            
            user_ids = evento.get('assistants', [])        
            assistants = [{str("nombreCompleto"): user["completedName"], str("relacion"): user["relationship"]} for user in users_collection.find({'_id': {'$in': [ObjectId(id) for id in user_ids]}})]
            print(assistants)
            return render(request, 'informEvent.html', {
                'titulo': evento.get('title', ''),
                'categorias': evento.get('categories', []),
                'fecha': evento.get('date', ''),
                'lugar': evento.get('lugar', ''),
                'descripcion': evento.get('description', ''),
                'programas': evento.get('programs', []),
                'facultades': evento.get('facultades', []),
                'conferencistas': speakers,
                'asistentes': assistants,
                'comentarios': evento.get('comments', []),
                'users': users,
            })

