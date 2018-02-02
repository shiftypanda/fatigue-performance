# Generated by Django 2.0.1 on 2018-02-02 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rota', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actualshift',
            name='actual_shift_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rota.RotaShift'),
        ),
        migrations.AlterField(
            model_name='rotashift',
            name='rota_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rota.ShiftPattern'),
        ),
    ]