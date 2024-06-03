from django.urls import path
from django.views.generic import RedirectView
from .views import views_home, evento
from .views import *

urlpatterns = [
    path('', views_home.homeView, name='home'),

    path('eventos/', EventsView.as_view(), name='evento'),
    path('crear_evento/', EventForm.as_view(), name='crear_evento'),
    path("user/<str:id>/", UserDetail.as_view(), name="user_detail"),
    path('evento/<str:event_id>/', EventDetailView.as_view(), name='event_detail'),
]
