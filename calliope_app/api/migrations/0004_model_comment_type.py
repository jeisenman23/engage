# Generated by Django 2.1.4 on 2019-06-14 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190614_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_comment',
            name='type',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
