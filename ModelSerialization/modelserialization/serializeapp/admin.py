from django.contrib import admin
from .models import Snippet, Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [ 'student_id','name', 'year']

