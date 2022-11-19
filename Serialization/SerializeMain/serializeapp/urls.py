from django.urls import path
from serializeapp.views import SnippetApi,StudentListDetails,StudentIdentity,StudentList,StudentCreate,StudentUpdateDelete


urlpatterns = [
    path('<int:id>/',view=StudentIdentity,name='identity'),
    path('list/',view=StudentList,name='list'),
    path('create/',view=StudentCreate,name='create'),
    path('student/',view=StudentListDetails,name='list_details'),
    path('updatedelete/',view=StudentUpdateDelete,name='list_update'),
    path('snippet/',SnippetApi.as_view(),name='snippet_api')
]

