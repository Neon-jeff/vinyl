from django.urls import path
from .views import *

urlpatterns = [
    path("register/",RegisterUser,name='register' ),
    path("success/",RegisterSuccess,name='success'),
    path('login/',Login,name='login'),
    path('user/dashboard',Dashboard,name='dashboard')
]
