from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.Doctors.models import *
from apps.api.serializers import PersonaSerializer


class Personas(APIView):
    def get(self, request):
        personas = Persona.objects.all()
        personas_json = PersonaSerializer(personas, many=True)
        return Response(personas_json.data)

    def post(self, request):
        persona_json = PersonaSerializer(data=request.data)
        if persona_json.is_valid():
            persona_json.save()
            return Response(persona_json.data, status=201)
        return Response(persona_json.errors, status=400)


class PersonaDetails(APIView):
    def get_objetc(self, pk):
        try:
            return Persona.objects.get(pk=pk)
        except Persona.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        persona = self.get_objetc(pk)
        persona_json = PersonaSerializer(persona)
        return Response(persona_json.data)

    def put(self, request, pk):
        persona = self.get_objetc(pk)
        persona_json = PersonaSerializer(persona, data=request.data)
        if persona_json.is_valid():
            persona_json.save()
            return Response(persona_json.data)
        return Response(persona_json.errors, status=401)

    def delete(self, request, pk):
        persona = self.get_objetc(pk)
        persona.delete()
        return Response(status=204)

class SignosVitales(APIView):
    pass