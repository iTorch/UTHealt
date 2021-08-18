from django.http import request
from django.urls import path
app_name = "doctor"
from .views import *

urlpatterns = [
    #path('signos/',PacienteSignos.as_view(),name='Signos_paciente'),
    #path('doctor/buscar/',SignosList.as_view(), name = 'buscar'),
    #path('doctor/buscar/',buscarPac(request), name='buscar'),

    #ruta de la vista basada en clase del doctor index
    path('doctor/',PacientesList.as_view(), name = 'index'),

    #ruta de la vista basada en clase del doctor detalle del paciente 
    path('doctor-detalle/<int:pk>/', PacienteDetalle.as_view(), name = 'detalle'),
    
    
    ]