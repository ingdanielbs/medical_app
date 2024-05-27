# Generated by Django 5.0.6 on 2024-05-24 13:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctors', '0001_initial'),
        ('patients', '0002_rename_adress_patient_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_appointment', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='doctors.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='patients.patient')),
            ],
        ),
    ]
