from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View,generic
from django.views.generic import ListView, DetailView
from apps.Doctors.models import Persona, SignosVitales
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.



    
#clase para el index del doctor 
class PacientesList(ListView):
    #llamada al modelo de personas 
    model = Persona
    template_name = 'doctor/indexDoctor.html'
    
    #decorador de los metodos POST
    @method_decorator(csrf_exempt)
    def dispatch(self,request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self,request, *args, **kwargs):
        #regreso de todos los datos del ID     
        doc = {}
        doc = Persona.objects.get(pk = request.POST['id']).toJson()
        return JsonResponse(doc)


class PacienteDetalle(DetailView):
    #carga del modelo de personas para el template de detalle 
    model = Persona
    template_name = 'doctor/buscar.html'

    
    def get_context_data(self, **kwargs):
        #se optiene el data del id 
        context = super().get_context_data(**kwargs)
        #se genera el nuevo contexto y el modelo signos con base al id 
        context['signos'] = SignosVitales.objects.filter(id_persona= self.kwargs['pk'])
        #se regresa el contexto 
        return context