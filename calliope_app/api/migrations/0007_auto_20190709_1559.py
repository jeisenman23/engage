# Generated by Django 2.1.4 on 2019-07-09 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_model_snapshot_base'),
    ]

    operations = [
        migrations.AddField(
            model_name='loc_tech_param',
            name='timeseries_meta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Timeseries_Meta'),
        ),
        migrations.AddField(
            model_name='tech_param',
            name='timeseries_meta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Timeseries_Meta'),
        ),
    ]
