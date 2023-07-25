from django.shortcuts import render

# Create your views here.

def RegisterUser(request):
    if request.method=='POST':
        print(request.POST)
    return render(request,'pages/register.html')
