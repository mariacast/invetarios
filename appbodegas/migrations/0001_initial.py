# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-07-05 07:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('codigo', models.IntegerField()),
                ('marca', models.CharField(max_length=20)),
                ('serie', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RecursoUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recurso', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='appbodegas.Recurso')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.IntegerField()),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='recursousuario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='appbodegas.Usuario'),
        ),
        migrations.AddField(
            model_name='historial',
            name='recurso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='appbodegas.Recurso'),
        ),
        migrations.AddField(
            model_name='historial',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='appbodegas.Usuario'),
        ),
    ]
