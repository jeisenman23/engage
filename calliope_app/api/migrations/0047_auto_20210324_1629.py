# Generated by Django 2.2.13 on 2021-03-24 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0046_model_is_uploading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scenario_param',
            name='value',
            field=models.TextField(),
        ),
    ]
