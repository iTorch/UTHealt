from rest_framework import serializers
from apps.Doctors.models import Persona, Historial, PersonaMedico, SignosVitales

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class HistorialSerializer(serializers.ModelSerializer):
    pass
class PersonaMedicoSerializer(serializers.ModelSerializer):
    pass
class SignosVitalesSerializer(serializers.ModelSerializer):
    pass


