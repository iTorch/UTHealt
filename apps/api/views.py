from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.Doctors.models import *
from apps.api.serializers import PersonaMedicoSerializer, PersonaSerializer, HistorialSerializer, SignosVitalesSerializer


class PersonasView(APIView):
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
        return Response(persona_json.errors, status=400 )

    def delete(self, request, pk):
        persona = self.get_objetc(pk)
        persona.delete()
        return Response(status=204)


class SignosVitalesView(APIView):
    def get(self, request):
        signos = SignosVitales.objects.all()
        signos_serializer = SignosVitalesSerializer(signos, many=True)
        return Response(signos_serializer.data)

    def post(self, request):
        signos_serializer = SignosVitalesSerializer(data=request.data)
        if signos_serializer.is_valid():
            signos_serializer.save()
            return Response(signos_serializer.data, status=201)
        return Response(signos_serializer.errors, status=400)


class SignosVitalesDetails(APIView):
    def get_object(self, pk):
        try:
            return SignosVitales.objects.get(pk=pk)
        except SignosVitales.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        signos = self.get_object(pk)
        signos_serializer = SignosVitalesSerializer(signos)
        return Response(signos_serializer.data)

    def put(self, request, pk):
        signos = self.get_object(pk)
        signos_serializer = SignosVitalesSerializer(signos, data=request.data)
        if signos_serializer.is_valid():
            signos_serializer.save()
            return Response(signos_serializer.data)
        return Response(signos_serializer.errors, status=400)

    def delete(self, request, pk):
        signos = self.get_object(pk)
        signos.delete()
        return Response(status=204)


class PersonaMedicoView(APIView):
    def get(self, request):
        medico = PersonaMedico.objects.all()
        medico_serializer = PersonaMedicoSerializer(medico, many=True)
        return Response(medico_serializer.data)

    def post(self, request):
        medico_serializer = PersonaMedicoSerializer(data=request.data)
        if medico_serializer.is_valid():
            medico_serializer.save()
            return Response(medico_serializer.data, status=201)
        return Response(medico_serializer.errors, status=400)


class PersonaMedicoDetails(APIView):
    def get_object(self, pk):
        try:
            return PersonaMedico.objects.get(pk=pk)
        except PersonaMedico.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        medico = self.get_object(pk)
        medico_serializer = PersonaMedicoSerializer(medico)
        return Response(medico_serializer.data)

    def put(self, request, pk):
        medico = self.get_object(pk)
        medico_serializer = PersonaMedicoSerializer(medico, data=request.data)
        if medico_serializer.is_valid():
            medico_serializer.save()
            return Response(medico_serializer.data)
        return Response(medico_serializer.errors, status= 400)

    def delete(self, request, pk):
        medico = self.get_object(pk)
        medico.delete()
        return Response(status=204)


class HistorialView(APIView):
    def get(self, request):
        historial = Historial.objects.all()
        historial_serialize = HistorialSerializer(historial, many=True)
        return Response(historial_serialize.data)

    def post(self, request):
        historial_serialize = HistorialSerializer(data=request.data)
        if historial_serialize.is_valid():
            historial_serialize.save()
            return Response(historial_serialize.data, status=201)
        return Response(historial_serialize.errors, status=400)


class HistorialDetails(APIView):
    def get_object(self, pk):
        try:
            return Historial.objects.get(pk=pk)
        except Historial.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        historial = self.get_object(pk)
        historial_serialize = HistorialSerializer(historial)
        return Response(historial_serialize.data)

    def put(self, request, pk):
        historial = self.get_object(pk)
        historial_serialize = HistorialSerializer(historial, data=request.data)
        if historial_serialize.is_valid():
            historial_serialize.save()
            return Response(historial_serialize.data)
        return Response(historial_serialize.errors, status=400)

    def delete(self, request, pk):
        historial = self.get_object(pk)
        historial.delete()
        return Response(status=204)