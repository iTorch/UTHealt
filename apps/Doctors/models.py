# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.forms.models import model_to_dict

class Historial(models.Model):
    id_historial = models.AutoField(primary_key=True)
    id_signos_vitales = models.ForeignKey('SignosVitales', on_delete=models.RESTRICT,  db_column='id_signos_vitales')
    fecha_actual = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'historial'


class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    genero = models.CharField(max_length=1, choices=[('H', 'Hombre'), ('M', 'Mujer')])
    fecha_nacimiento = models.DateField(blank=True, null=True)
    altura = models.FloatField()
    peso = models.FloatField()
    ciudad = models.CharField(max_length=50)
    codigo_postal = models.IntegerField()
    colonia = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'persona'
    
    def toJson(self):
        item = model_to_dict(self)
        return item


class PersonaMedico(models.Model):
    id_persona_medico = models.AutoField(primary_key=True)
    cedula_medica = models.CharField(max_length=50)
    id_persona = models.ForeignKey(Persona, on_delete=models.PROTECT, db_column='id_persona', blank=True, null=True)

    class Meta:
        db_table = 'persona_medico'


class SignosVitales(models.Model):
    id_signos_vitales = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(Persona, on_delete=models.PROTECT, db_column='id_persona')
    oxigeno = models.IntegerField()
    temperatura = models.FloatField()
    calorias_quemadas = models.FloatField()
    pasos_diario = models.IntegerField()
    distancia_recorrida = models.FloatField()
    ritmo_cardiaco = models.FloatField()

    class Meta:
        db_table = 'signos_vitales'

    def toJson(self):
        item = model_to_dict(self)
        return item
