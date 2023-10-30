
from django.urls import path
from . views import register,Userlogin

urlpatterns = [
    path('register/',register.as_view()),
    path('login/',Userlogin.as_view()),
]