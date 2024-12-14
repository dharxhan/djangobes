from django.db import models

# Create your models here.
class Employee(models.Model):
    name= models.CharField(max_length=255, default="Name") 
    email=models.EmailField(help_text="Enter a valid eMail address")
    designation = models.CharField(max_length=255, blank=True, null=True)
    joindate=models.DateField()
