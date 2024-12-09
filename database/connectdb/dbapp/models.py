from django.db import models

# Create your models here.
class student(models.Model):
    rno=models.IntegerField()
    name=models.CharField(max_length=30)
    marks=models.FloatField()
    city=models.CharField(max_length=30)
    fees=models.FloatField()