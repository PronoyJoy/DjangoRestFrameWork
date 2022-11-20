from django.urls import path
from .views import student_info

urlpatterns = [
    path('1/',view=student_info)
]
