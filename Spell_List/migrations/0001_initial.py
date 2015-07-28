# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterClass',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('is_ritual', models.BooleanField(default=False)),
                ('is_concentration', models.BooleanField(default=False)),
                ('level', models.PositiveSmallIntegerField(default=0)),
                ('school', models.CharField(max_length=255)),
                ('casting_time', models.CharField(max_length=255)),
                ('duration', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('canBeCastBy', models.ManyToManyField(to='Spell_List.CharacterClass')),
                ('components', models.ManyToManyField(to='Spell_List.Component')),
            ],
        ),
    ]
