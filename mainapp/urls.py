from django.urls import path
from .views import views_home
from .views.evento import *
from .views.viewsEventoInfo import *

urlpatterns = [
    path('', views_home.homeView, name='home'),

    path('eventos/', EventsView.as_view(), name='evento'),
    path('crear_evento/', EventForm.as_view(), name='crear_evento'),
    path('evento/<str:event_id>/', EventDetailView.as_view(), name='event_detail'),
]
