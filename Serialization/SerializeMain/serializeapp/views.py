from django.shortcuts import render
from . models import Student,Snippet
from .serializers import StudentSerializer,SnippetSerializer
from django.views import View
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from django.utils.decorators import method_decorator

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
        


@csrf_exempt
def StudentListDetails(request):
    if request.method == 'GET': #json to python
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        student_id = py_data.get('student_id', None)# get id from py_Data

        if student_id is not None:
            student_obj = Student.objects.get(student_id = student_id)
            serializer = StudentSerializer(student_obj)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        
        student_obj = Student.objects.all()
        serializer = StudentSerializer(student_obj,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method == 'POST': #create
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=py_data)

        if serializer.is_valid():
            serializer.save()
            res = {'msg':'created successfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')

        json_data= JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
        


@csrf_exempt
def StudentUpdateDelete(request):
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        student_id = py_data.get('student_id') #get that specific id 
        student_obj = Student.objects.get(student_id = student_id) #find out the student by filtering id
        serializer = StudentSerializer(student_obj, data=py_data, partial = True) #transfer data to databse mapping

        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Updated Successfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        student_id = py_data.get('student_id')
        student_obj = Student.objects.get(student_id = student_id)
        student_obj.delete()
        res = {'msg':'Deleted Successfully'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')

    


@method_decorator(csrf_exempt,name='dispatch')
class SnippetApi(View):

    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        title = py_data.get('title',None)
        if title is not None:
            snippet_obj = Snippet.objects.get(title=  title)
            serializer = SnippetSerializer(snippet_obj)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        snippet_obj = Snippet.objects.all()
        serializer = SnippetSerializer(snippet_obj,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    
    def post(self, request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream)
        serializer = SnippetSerializer(data=py_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'created successfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')




        