from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
# Create your views here.
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io

def StudentIdentity(request,id):
    user = Student.objects.get(id=id)
    serializer = StudentSerializer(user)
    data = JSONRenderer().render(serializer.data)
    return HttpResponse(data, content_type='application/json')

def StudentList(request):
    user = Student.objects.all()
    serializer = StudentSerializer(user,many=True)
    data = JSONRenderer().render(serializer.data)
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def StudentCreate(request):
    if request.method == 'POST':
        data = request.body
        stream = io.BytesIO(data)
        py_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=py_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created'}
            json_data= JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data= JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
        



