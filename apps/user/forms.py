from django import forms
from apps.Doctors.models import Persona
from apps.user.models import User



class FormPersona(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        #widgets = {'fecha_nacimiento': forms.DateField(attrs={'type':'date'})}

class FormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',]