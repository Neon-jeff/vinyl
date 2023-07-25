from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
import uuid
# Create your views here.

def RegisterUser(request):
    used_uname='nw'
    used_email='nw'
    if request.method=='POST':
        used_uname=User.objects.filter(username=request.POST.get('uname')).first()
        used_email=User.objects.filter(username=request.POST.get('email')).first()
        if used_uname ==None and used_email==None:
            user=User.objects.create(
                username=request.POST['uname'],
                email=request.POST['email']
            )
            user.set_password(request.POST['password'])
            user.save()
            profile=UserProfile.objects.create(
                user=user,
                full_name=request.POST['fname']
            )
            profile.token=str(uuid.uuid4())
            profile.save()
            return redirect('success')
        elif used_uname!=None:
            print("uname used")
        elif used_email!=None:
            print("email used")
    return render(request,'pages/register.html',{'email':used_email,'uname':used_uname})

def RegisterSuccess(request):
    return render(request,'pages/regsucess.html')
