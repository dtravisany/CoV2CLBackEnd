# Generated by Django 3.0.8 on 2020-08-07 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cov2cl', '0011_remove_sample_location_exposure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='sex',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='title',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
