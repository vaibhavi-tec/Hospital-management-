# Generated by Django 4.1.1 on 2024-09-18 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='med',
            name='record_id',
            field=models.CharField(blank=True, editable=False, max_length=255),
        ),
    ]
