# Generated by Django 4.1.1 on 2024-09-18 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('patient_name', models.CharField(max_length=255)),
                ('appointment_id', models.CharField(blank=True, editable=False, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('appointment_date', models.DateField()),
                ('appointment_from', models.TimeField()),
                ('appointment_to', models.TimeField()),
                ('gender', models.CharField(max_length=10)),
                ('doctor_name', models.CharField(max_length=10)),
                ('condition', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Equip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_id', models.CharField(blank=True, editable=False, max_length=255, unique=True)),
                ('equipment_name', models.CharField(editable=False, max_length=100)),
                ('equipment_status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('item_name', models.CharField(max_length=100)),
                ('inventory_id', models.CharField(blank=True, editable=False, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('quantity', models.CharField(max_length=255)),
                ('supplier', models.CharField(max_length=100)),
                ('cost', models.IntegerField()),
                ('stock_level', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.TextField()),
                ('laboratory_test', models.CharField(editable=False, max_length=20)),
                ('laboratory_ID', models.CharField(blank=True, editable=False, max_length=255, unique=True)),
                ('cost_of_service', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ref_doctor', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Med',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_id', models.CharField(blank=True, editable=False, max_length=255, unique=True)),
                ('patient_id', models.TextField(blank=True, editable=False, max_length=255, unique=True)),
                ('doctor_id', models.TextField(blank=True, editable=False, max_length=255, unique=True)),
                ('diagnosis', models.TextField(editable=False, max_length=100)),
                ('treatment', models.TextField(editable=False, max_length=100)),
                ('prescriptions', models.TextField(editable=False, max_length=100)),
                ('test_results', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, unique=True)),
                ('password', models.CharField(max_length=10)),
                ('role', models.CharField(max_length=255)),
            ],
        ),
    ]
