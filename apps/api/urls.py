from django.urls import path

from apps.api.views import *

urlpatterns = [
    path('', Login.as_view(), name = "login"),
    path('logout/', Logout.as_view(), name = "logout"),
    path('personas/', PersonasView.as_view(), name='personas_list'),
    path('signos/', SignosVitalesView.as_view(), name='signos_list'),
    path('medicos/', PersonaMedicoView.as_view(), name='medicos_list'),
    path('historiales/', SignosVitalesView.as_view(), name='historiales_list'),
    path('persona/<int:pk>/', PersonaDetails.as_view(), name='persona_details'),
    path('signo/<int:pk>/', SignosVitalesDetails.as_view(), name='signos_details'),
    path('medico/<int:pk>/', PersonaMedicoDetails.as_view(), name='medico_details'),
    path('historial/<int:pk>/', HistorialDetails.as_view(), name='historial_details'),
]