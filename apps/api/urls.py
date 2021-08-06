from django.urls import path

from apps.api.views import Personas, PersonaDetails

urlpatterns = [
    path('personas/', Personas.as_view(), name='personas_list'),
    path('persona/<int:pk>/', PersonaDetails.as_view(), name='personas_detail')
]