from django.http import request
from django.urls import path
app_name = "doctor"
from .views import *
urlpatterns = [
    #path('signos/',PacienteSignos.as_view(),name='Signos_paciente'),
    path('doctor/',PacientesList.as_view(), name = 'index'),
    path('<int:pk>/', PacienteDetalle.as_view(), name = 'detalle'),
    #path('doctor/buscar/',SignosList.as_view(), name = 'buscar'),
    #path('doctor/buscar/',buscarPac(request), name='buscar'),
    #path('doctor/buscar/',buscarPac, name='buscar'),
    ]