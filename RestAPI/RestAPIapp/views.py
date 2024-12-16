from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view()
def say_hello(request):
    return Response({"statuscode":200, "message": "Hello World!"})