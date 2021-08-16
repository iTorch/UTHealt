from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.Doctors.models import Persona
# Create your models here.

class User(AbstractUser):
    persona = models.ForeignKey(Persona, on_delete=models.RESTRICT, db_column='id_persona', blank=True, null=True)

    #Renombrar el metodo
    #def save(self,*args,**kwargs):
        #if self.pk is None:
            #self.set_password(self.password)
        #super().save(*args,**kwargs)


