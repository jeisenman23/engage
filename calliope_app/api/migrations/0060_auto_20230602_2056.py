# Generated by Django 3.2.16 on 2023-06-02 20:56

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0059_auto_20230104_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameter',
            name='choices',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='units',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('rate_unit', models.CharField(max_length=20)),
                ('quantity_unit', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('deleted', models.DateTimeField(default=None, editable=False, null=True)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.model')),
            ],
            options={
                'verbose_name_plural': '[2] Carriers',
                'db_table': 'carrier',
                'ordering': ['name'],
                'unique_together': {('model', 'name')},
            },
        ),
    ]
