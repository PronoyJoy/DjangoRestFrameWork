from django.urls import path
from .views import UserRegistraion,UserLoginView

urlpatterns = [
    path('signup/',UserRegistraion.as_view(),name='signup'),
    path('login/',UserLoginView.as_view(),name='login')
]
