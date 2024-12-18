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

@api_view(['POST'])
def postdata(request):
    #data = request.data
    #return Response({'statuscode':200, 'data':data, 'message':'success'})
    serializer = EmployeeSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'statuscode':400,'data':serializer.errors, 'message':'Invalid data'})
    serializer.save()
    return Response({'statuscode':201, 'data':serializer.data, 'message':'success'})

@api_view(['PUT'])
def putdata(request,pk):
    #data = request.data
    #return Response({'statuscode':200, 'data':data, 'message':'success'})
    try:
        employee=Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(employee,data=request.data)
        if not serializer.is_valid():
            return Response({'statuscode':400,'data':serializer.errors, 'message':'Invalid data'})
        serializer.save()
        return Response({'statuscode':201, 'data':serializer.data, 'message':'success'})
    except: 
        return Response({'statuscode':404, 'data':'not found','message':'Employee not found'})