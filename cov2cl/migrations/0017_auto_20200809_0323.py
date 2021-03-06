# Generated by Django 3.0.8 on 2020-08-09 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cov2cl', '0016_mature_protein_region_of_cds'),
    ]

    operations = [
        migrations.CreateModel(
            name='utrs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='mature_protein_region_of_cds',
            name='pdblink',
        ),
        migrations.RemoveField(
            model_name='mature_protein_region_of_cds',
            name='uniprotlink',
        ),
        migrations.CreateModel(
            name='stem_loop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('dbxref_gene_id', models.IntegerField()),
                ('function', models.CharField(max_length=500)),
                ('inference', models.CharField(max_length=300)),
                ('locus_tag', models.CharField(max_length=100)),
                ('gene', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contains', to='cov2cl.gene')),
            ],
        ),
    ]
