# Generated by Django 3.0.6 on 2020-07-31 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cov2cl', '0010_auto_20200731_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='gisaidclades',
            name='mutation',
            field=models.ManyToManyField(related_name='variationGisaid', to='cov2cl.Mutations'),
        ),
        migrations.AddField(
            model_name='nextstrainclades',
            name='mutation',
            field=models.ManyToManyField(related_name='variationNextstrain', to='cov2cl.Mutations'),
        ),
        migrations.AddField(
            model_name='pangolinlineage',
            name='mutation',
            field=models.ManyToManyField(related_name='variationPangolin', to='cov2cl.Mutations'),
        ),
    ]
