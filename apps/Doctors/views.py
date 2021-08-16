from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View,generic
from django.views.generic import ListView
from apps.Doctors.models import Persona, SignosVitales
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta
# Create your views here.


def indexDoctor(request):
    #p = Persona.objects.filter(nombre = "edgar").order_by('nombre')#filtrar pacientes 
    p =Persona.objects.all().order_by('nombre')
    if len(p)>0:
        pacientes = {'pacientes':p,}
        print(pacientes)
        return render(request, 'doctor/indexDoctor.html',pacientes )
    else: 
        data = {'msg':'Error no hay pacientes registrados', }

"""def sigPacientes(request):

    sv = SignosVitales.objects.filter(id_persona = 1)
    if len(sv)>0:

        signos = {'signos':sv}
        print(signos)
        return render(request,'doctor/signosDoctor.html',signos)
    else:
        return render(request, 'doctor/indexDoctor.html',{'status':'Error',})"""

def buscarPac(request):
    
        bp =Persona.objects.filter(id_persona="1")
        if len(bp)>0:
            #se hace el recorrido 
            for bs in bp:
                id = bs.id_persona
                fN = bs.fecha_nacimiento

            #se calcula la edad con base a la fecha actual
            edad = relativedelta(datetime.now(), fN)
            e = str((edad.years))
 
            bs = SignosVitales.objects.filter(id_persona = id)
            bus = {'buPacs':bp,'edadT':e,'busSig':bs}
            # print(bus)
            return render(request, 'doctor/buscar.html',bus )
        else: 
            data = {'msg':'Error no hay pacientes registrados', }
            return render(request, 'indexDoctor/indexDoctor.html',data )
    

class PacientesList(ListView):
    model = Persona
    template_name = 'doctor/indexDoctor.html'
    

    """def dispatch(request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)"""

    def post(self,request, *args, **kwargs):
        p = Persona.objects.get(id_persona = '2').toJson()
        data = {'msg':p}
        #se comprueba que hay en el body 
        #print(request.POST)


        return JsonResponse(data)

        #funcion que me retorna todo del modelo 
    """ def get_queryset(self):
        #retorna nombres que empiecen con 
        #return Persona.objects.filter(nombre__startswith="ed")

        #retorna todo del modelo
        return Persona.objects.all()

        #retorna nombre con edgar
        #return Persona.objects.filter(nombre = 'edgar')"""
    


    
        