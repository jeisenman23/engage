# Generated by Django 2.1.4 on 2019-08-05 05:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20190805_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeseries_meta',
            name='file_uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]