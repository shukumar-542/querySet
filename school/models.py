from django.db import models

# Create your models here.

class Student(models.Model):
      name = models.CharField(max_length=50)
      roll= models.IntegerField(unique=True, null=False)
      city = models.CharField(max_length=50)
      result= models.IntegerField()
      pass_date= models.DateField()


class Teacher(models.Model):
      name = models.CharField(max_length=50)
      empid= models.IntegerField(unique=True, null=False)
      city = models.CharField(max_length=50)
      salary= models.IntegerField()
      join_date= models.DateField()


