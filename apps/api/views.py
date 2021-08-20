from django.contrib.sessions.models import Session
from datetime import datetime
from django.http import Http404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.Doctors.models import *
from apps.api.serializers import PersonaMedicoSerializer, PersonaSerializer, HistorialSerializer, SignosVitalesSerializer
from apps.api.serializers import UserTokenSerializer

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


class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context={'request': request})
        if login_serializer.is_valid():
            print(login_serializer.validated_data["user"])
            user = login_serializer.validated_data['user']
            print(user.persona)
            if user.is_active:
                token,created = Token.objects.get_or_create(user = user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response({
                        'token' : token.key,
                        'user': user_serializer.data,
                        'mensaje' : 'Inicio de Sesion Exitoso'
                    }, status = status.HTTP_201_CREATED)
                else:
                    """Eliminar Sesiones
                    all_sessions = Session.objects.filter(expire_date__gt= datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    Eliminar Sesiones"""
                    """Renovar Token"""
                    token.delete()
                    token = Token.objects.create(user = user)
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'mensaje': 'Inicio de Sesion Exitoso'
                    }, status=status.HTTP_201_CREATED)
                    """Renovar Token"""
                    """Bloquear inicio de sesion y borrar token
                    token.delete()
                    return Response({'error': 'Ya se ha iniciado sesion con este usuario'},
                                    status = status.HTTP_409_CONFLICT)
                    Bloquear inicio de sesion y borrar token"""
            else:
                return Response({'error': 'Este usuario no puede inicar sesion'},
                                status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Nombre de usuario o contraseña incorrectos'},
                            status= status.HTTP_400_BAD_REQUEST)
        return Response({"msj": "Hola"}, status= status.HTTP_200_OK)

class Logout(APIView):
    def post(self, request, *arg, **kwargs):
        try:
            token = request.data['token']
            token = Token.objects.filter(key = token).first()
            if token:
                user = token.user

                all_sessions = Session.objects.filter(expire_date__gt=datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()

                token.delete()

                session_message = 'Sesiones de usuario eliminadas'
                token_message = 'Token eliminado'
                return Response({'token_message': token_message,'session_message': session_message, 'status': 'Sesion cerrada correctamente'},
                                status = status.HTTP_200_OK)

            return Response({'error':'No se ha encontrado un usuario con estas credenciales'},
                            status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'Token Invalido'}, status=status.HTTP_409_CONFLICT)