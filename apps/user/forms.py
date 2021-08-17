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
        fields = ['username','email','password','groups']
        widgets = {'password': forms.PasswordInput(),
                   'groups': forms.SelectMultiple(
                       attrs={
                            'name':'groups',
                            'id':'groups',
                            'onChange' : "showInp();"
                   })}
        exclude =['last_login','is_superuser','first_name','last_name','is_staff','is_active','persona', 'user_permissions', 'date_joined']



















