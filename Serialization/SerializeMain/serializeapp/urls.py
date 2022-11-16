from django.urls import path
from serializeapp.views import StudentIdentity,StudentList,StudentCreate


urlpatterns = [
    path('<int:id>/',view=StudentIdentity,name='identity'),
    path('list/',view=StudentList,name='list'),
    path('create/',view=StudentCreate,name='create')
]
