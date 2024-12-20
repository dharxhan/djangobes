from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
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
    try:
        employee=Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(employee,data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'statuscode':403,'error':serializer.errors, 'message':'Something went wrong'})
        serializer.save()
        return Response({'statuscode':200, 'payload':serializer.data, 'message':'Data saved successfully'})
    except Exception as e: 
        return Response({'statuscode':500, 'erroe':str(e),'message':'Something went wrong'})
    
@api_view(['PATCH'])
def patchdata(request,pk):
    try:
        employee=Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(employee,data=request.data,partial=True)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'statuscode':403,'error':serializer.errors, 'message':'Something went wrong'})
        serializer.save()
        return Response({'statuscode':200, 'payload':serializer.data, 'message':'Data saved successfully'})
    except Exception as e: 
        return Response({'statuscode':500, 'erroe':str(e),'message':'Something went wrong'})

@api_view(['DELETE'])
def deletedata(request,pk):
    try:
        employee=Employee.objects.get(id=pk)
        employee.delete()
        return Response({'statuscode':200, 'message':'Data deleted successfully'})
    except Exception as e:
        return Response({'statuscode':500, 'error':str(e),'message':'Something went wrong'})

class EmployeeApiView(APIView):
    def get(self, request, pk=None):
        if pk:
            employee = Employee.objects.get(id=pk)  # Renamed to avoid shadowing
            serializer = EmployeeSerializer(employee, many=False)
            return Response(serializer.data)
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'statuscode':400,'data':serializer.errors, 'message':'Invalid data'})
        serializer.save()
        return Response({'statuscode':201, 'data':serializer.data, 'message':'success'})
    
    def put(self, request, pk):
        try:
            employee=Employee.objects.get(id=pk)
            serializer = EmployeeSerializer(employee,data=request.data)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'statuscode':403,'error':serializer.errors, 'message':'Something went wrong'})
            serializer.save()
            return Response({'statuscode':200, 'payload':serializer.data, 'message':'Data saved successfully'})
        except Exception as e: 
            return Response({'statuscode':500, 'erroe':str(e),'message':'Something went wrong'})
        
    def putdata(request,pk):
        try:
            employee=Employee.objects.get(id=pk)
            serializer = EmployeeSerializer(employee,data=request.data)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'statuscode':403,'error':serializer.errors, 'message':'Something went wrong'})
            serializer.save()
            return Response({'statuscode':200, 'payload':serializer.data, 'message':'Data saved successfully'})
        except Exception as e: 
            return Response({'statuscode':500, 'erroe':str(e),'message':'Something went wrong'})