# Generated by Django 3.0.6 on 2020-07-31 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cov2cl', '0015_auto_20200731_1742'),
    ]

    operations = [
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
    ]
