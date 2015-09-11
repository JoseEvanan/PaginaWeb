# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('buscar', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=50)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('dni', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_persona', models.CharField(max_length=15, choices=[(b'T', b'Trabajador'), (b'V', b'Visitante')])),
            ],
        ),
        migrations.AddField(
            model_name='cita',
            name='registros',
            field=models.ForeignKey(to='registro.Registro'),
        ),
    ]
