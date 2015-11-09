# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corredor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=40)),
                ('apellidoPaterno', models.CharField(max_length=30)),
                ('apellidoMaterno', models.CharField(max_length=30)),
                ('edad', models.CharField(max_length=30)),
                ('sexo', models.CharField(max_length=2, choices=[(b'm', b'Masculino'), (b'f', b'Femenino')])),
                ('lorigen', models.CharField(max_length=50)),
                ('lresidencia', models.CharField(max_length=50)),
                ('correoElectronico', models.EmailField(max_length=60)),
                ('direccion', models.CharField(max_length=70)),
                ('codigoPostal', models.IntegerField(max_length=5)),
                ('estado', models.CharField(max_length=25)),
                ('ciudad', models.CharField(max_length=25)),
                ('telefono', models.CharField(max_length=20)),
                ('celular', models.CharField(max_length=20)),
                ('equipo', models.CharField(max_length=70)),
            ],
        ),
    ]
