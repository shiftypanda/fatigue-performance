# Generated by Django 2.0.1 on 2018-02-02 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShiftPattern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift_name', models.CharField(max_length=40)),
                ('start_time', models.TimeField()),
                ('finish_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='RotaShift',
            fields=[
                ('shiftpattern_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rota.ShiftPattern')),
            ],
            bases=('rota.shiftpattern',),
        ),
        migrations.CreateModel(
            name='ActualShift',
            fields=[
                ('rotashift_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rota.RotaShift')),
            ],
            bases=('rota.rotashift',),
        ),
        migrations.AddField(
            model_name='rotashift',
            name='rota_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RotaShift', to='rota.ShiftPattern'),
        ),
        migrations.AddField(
            model_name='actualshift',
            name='actual_shift_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ActualShift', to='rota.RotaShift'),
        ),
    ]