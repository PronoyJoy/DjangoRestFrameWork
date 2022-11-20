from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET','POST'])
def student_info(request):
    if request.method == 'GET':
        return Response({ "msg": "GET", "data": request.data})

    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})

    
    
