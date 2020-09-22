# Generated by Django 3.0.6 on 2020-05-17 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cov2cl', '0004_auto_20200513_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='cou_sampled', to='cov2cl.Location'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='country_exposure',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='cou_exposure', to='cov2cl.Location'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='division',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='div_sampled', to='cov2cl.Location'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='division_exposure',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='div_exposure', to='cov2cl.Location'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='loc_sampled', to='cov2cl.Location'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='location_exposure',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='loc_exposure', to='cov2cl.Location'),
        ),
    ]
