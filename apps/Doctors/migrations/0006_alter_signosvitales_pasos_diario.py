# Generated by Django 3.2.6 on 2021-08-16 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctors', '0005_rename_peso_diario_signosvitales_pasos_diario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signosvitales',
            name='pasos_diario',
            field=models.IntegerField(),
        ),
    ]
