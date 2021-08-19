from rest_framework import serializers
from apps.Doctors.models import Persona, Historial, PersonaMedico, SignosVitales
from apps.user.models import User


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'


class HistorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historial
        fields = '__all__'


class PersonaMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaMedico
        fields = '__all__'


class SignosVitalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignosVitales
        fields = '__all__'


class PersonaMovilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id_persona', 'nombre')


class UserTokenSerializer(serializers.ModelSerializer):
    persona = PersonaMovilSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'persona')


