# Generated by Django 3.0.6 on 2020-07-29 18:27
#Modificado por Dante Travisany

from django.db import migrations
from django.conf import settings


def create_data(apps, schema_editor):
    User = apps.get_model(settings.AUTH_USER_MODEL)
    user = User(pk=1, username="auth0user", is_active=True , email="dtravisany@dim.uchile.cl")
    user.save()


class Migration(migrations.Migration):
    dependencies = [
    ]
    operations = [
        migrations.RunPython(create_data),
    ]

