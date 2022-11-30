from django.urls import path
from serializeapp.views import StudentListDetails,StudentIdentity,StudentList,StudentCreate,StudentUpdateDelete


urlpatterns = [
    path('<int:id>/',view=StudentIdentity,name='identity'),
    path('list/',view=StudentList,name='list'),
    path('create/',view=StudentCreate,name='create'),
    path('student/',view=StudentListDetails,name='list_details'),
    path('updatedelete/',view=StudentUpdateDelete,name='list_update')
]

