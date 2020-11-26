# Generated by Django 3.0.4 on 2020-11-25 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sector_analysis', '0004_auto_20201122_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='holdings',
            name='exitdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='holdings',
            name='sell',
            field=models.FloatField(default=0.0),
        ),
    ]