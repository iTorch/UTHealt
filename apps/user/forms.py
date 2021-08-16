from django import forms
from django.forms import ModelForm

from apps.Doctors.models import *
from apps.user.models import User


class FormPersona(ModelForm):

    class Meta:
        model = Persona
        fields = '__all__'
        #widgets = {'fecha_nacimiento': forms.DateField()}




class FormUser(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'
        widgets = {'password': forms.PasswordInput(),}
        exclude =['last_login','is_superuser','first_name','last_name','is_staff','is_active','persona', 'user_permissions', 'date_joined']


class FormMP(forms.ModelForm):
    class Meta:
        model = PersonaMedico
        fields = '__all__'
        exclude =['id_persona']
















