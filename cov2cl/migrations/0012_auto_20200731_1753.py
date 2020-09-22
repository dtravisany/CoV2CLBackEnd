# Generated by Django 3.0.6 on 2020-07-31 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cov2cl', '0011_auto_20200731_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mutation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mutation', models.CharField(max_length=100)),
                ('reference', models.CharField(max_length=5)),
                ('query', models.CharField(max_length=5)),
                ('position', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='pangolinlineage',
            old_name='linage',
            new_name='lineage',
        ),
        migrations.AlterField(
            model_name='genome',
            name='pangolin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Pangolin_linage', to='cov2cl.PANGOLINLineage'),
        ),
        migrations.AlterField(
            model_name='pangolinlineage',
            name='father',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='PangolinFather', to='cov2cl.PANGOLINLineage'),
        ),
        migrations.RenameModel(
            old_name='GisaidClades',
            new_name='GISAIDClade',
        ),
        migrations.RenameModel(
            old_name='NextstrainClades',
            new_name='NextstrainClade',
        ),
        migrations.AlterField(
            model_name='gisaidclade',
            name='mutation',
            field=models.ManyToManyField(related_name='variationGisaid', to='cov2cl.Mutation'),
        ),
        migrations.AlterField(
            model_name='nextstrainclade',
            name='mutation',
            field=models.ManyToManyField(related_name='variationNextstrain', to='cov2cl.Mutation'),
        ),
        migrations.AlterField(
            model_name='pangolinlineage',
            name='mutation',
            field=models.ManyToManyField(related_name='variationPangolin', to='cov2cl.Mutation'),
        ),
    ]
