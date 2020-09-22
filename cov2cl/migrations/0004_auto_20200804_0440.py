# Generated by Django 3.0.8 on 2020-08-04 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cov2cl', '0003_auto_20200801_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='Name',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='division',
            name='Name',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='Name',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='Name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
