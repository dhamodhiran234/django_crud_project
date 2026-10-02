from django.db import models

# Create your models here.
class Sign(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)

class Adddata(models.Model):
    roll=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField(max_length=20)
    gender=models.CharField(max_length=20)
    address=models.CharField(max_length=100)