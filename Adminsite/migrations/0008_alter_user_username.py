# Generated by Django 4.1.1 on 2024-09-19 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminsite', '0007_patient_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, default='Patient', max_length=100, unique=True),
        ),
    ]
