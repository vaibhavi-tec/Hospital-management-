# Generated by Django 4.1.1 on 2024-09-18 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminsite', '0003_alter_med_doctor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='med',
            name='patient_id',
            field=models.TextField(blank=True, editable=False, max_length=255),
        ),
    ]
