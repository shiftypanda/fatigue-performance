# Generated by Django 2.0.5 on 2018-05-23 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rota', '0005_auto_20180523_0956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shift',
            old_name='start_date',
            new_name='start_time',
        ),
    ]
