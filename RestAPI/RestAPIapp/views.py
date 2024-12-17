from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Employee
from .serializers import EmployeeSerializer
# Create your views here.

#@api_view(['GET'])
def say_hello(request):
    return Response({"statuscode":200, "message": "Hello World!"})

@api_view(['GET'])
def getdata(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)