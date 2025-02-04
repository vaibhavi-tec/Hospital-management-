from django.db import models

class employee(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    utype=models.CharField(max_length=200)
