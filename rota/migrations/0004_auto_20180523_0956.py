# Generated by Django 2.0.5 on 2018-05-23 08:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rota', '0003_auto_20180523_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 23, 8, 56, 0, 886169, tzinfo=utc)),
        ),
    ]
