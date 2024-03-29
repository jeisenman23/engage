# Generated by Django 3.2.13 on 2022-06-05 03:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskmeta', '0003_batchtask'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0054_run_timestep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='run_task',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='model_run', to='taskmeta.celerytask'),
        ),
        migrations.CreateModel(
            name='ComputeEnvironment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('full_name', models.CharField(max_length=120)),
                ('is_default', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('Celery Worker', 'Celery Worker'), ('Container Job', 'Container Job'), ('Other Compute', 'Other Compute')], max_length=60)),
                ('ncpu', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('memory', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('cmd', models.TextField(blank=True, null=True)),
                ('users', models.ManyToManyField(blank=True, related_name='compute_environments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '[Admin] Compute Environment',
                'verbose_name_plural': '[Admin] Compute Environments',
                'db_table': 'compute_environments',
            },
        ),
        migrations.AddField(
            model_name='run',
            name='compute_environment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.computeenvironment'),
        ),
    ]
