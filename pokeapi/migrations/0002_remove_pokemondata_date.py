# Generated by Django 4.1.1 on 2022-09-19 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemondata',
            name='date',
        ),
    ]
