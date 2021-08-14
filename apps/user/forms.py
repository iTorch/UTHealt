from django import forms
from django.forms import PasswordInput, DateField
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from apps.Doctors.models import Persona
from apps.user.models import User



class FormPersona(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        #widgets = {'fecha_nacimiento': forms.DateField()}




class FormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'groups', ]
        widgets = {'password': forms.PasswordInput(),
                   'groups': forms.Select(attrs={
                       'placeholder':'------'
                   })
                   }

