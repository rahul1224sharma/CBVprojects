from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    pages=models.IntegerField()
    price=models.FloatField()

class Company(models.Model):
    name=models.CharField(max_length=40)
    location=models.CharField(max_length=50)
    ceo=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Employee(models.Model):
    eno=models.IntegerField()
    name=models.CharField(max_length=60)
    salary=models.FloatField()
    company=models.ForeignKey(Company,related_name='employees',on_delete=models.CASCADE)
