# Generated by Django 3.0.8 on 2020-09-09 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cov2cl', '0036_gene_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='gene',
            name='min_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
