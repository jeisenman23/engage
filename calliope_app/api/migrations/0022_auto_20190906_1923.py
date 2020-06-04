# Generated by Django 2.1.4 on 2019-09-06 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskmeta', '0001_initial'),
        ('api', '0021_model_user_last_access'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='build_task',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='build_run', to='taskmeta.CeleryTask'),
        ),
        migrations.AddField(
            model_name='run',
            name='run_task',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='model_run', to='taskmeta.CeleryTask'),
        ),
        migrations.AddField(
            model_name='timeseries_meta',
            name='upload_task',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='timeseries_meta', to='taskmeta.CeleryTask'),
        ),
    ]
