from rest_framework import serializers
from apps.Doctors.models import Persona, Historial, PersonaMedico, SignosVitales


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


