from django.urls import path
from .views import *

urlpatterns = [
    path("register/",RegisterUser,name='register' )
]
