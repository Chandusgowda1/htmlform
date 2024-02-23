from django.db import models

# Create your models here.

class registeration(models.Model):
    name=models.CharField(max_length=20)
    mobile=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()
    psw=models.CharField(max_length=20)
    gender=models.CharField(max_length=5)
    dob=models.DateField(default='23-12-2002')

class details(models.Model):
    name=models.CharField(max_length=20)
    phno=models.IntegerField()
    age=models.IntegerField()
    gender=models.CharField()
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class fb(models.Model):
    name=models.CharField(max_length=10)
    age=models.IntegerField()
    phno=models.IntegerField()
        