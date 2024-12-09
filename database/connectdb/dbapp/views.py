from django.shortcuts import render
from .models import*

# Create your views here.
def adddata(requests):
    sObj= Student()
    sObj.rno= 100
    sObj.name="Mohan"
    sObj.marks=450
    sObj.fees=100000
    sObj.city="Bangalore"