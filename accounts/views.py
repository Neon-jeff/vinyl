from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .models import *
from django.contrib.auth.models import User
import uuid
from django.contrib import messages
# Create your views here.

def RegisterUser(request):
    used_uname='nw'
    used_email='nw'
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method=='POST':
        used_uname=User.objects.filter(username=request.POST.get('uname')).first()
        used_email=User.objects.filter(email=request.POST.get('email')).first()
        if used_uname is None and used_email is None:
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

# Logs in the user

def Login(request):
    invalid=None
    noacc=None
    if request.user.is_authenticated:
        return redirect('dashboard')
    elif request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.filter(email=email).first()
        if user:
            print(user.username)
            auth_user=authenticate(username=user.username,password=password)
            if auth_user == None:
                invalid=True
            else:
                login(request, auth_user)
                return redirect('dashboard')
        else:
            noacc=True
        # return redirect('home')
    return render(request,'pages/login.html',{'noacc':noacc,'invalid':invalid})

def Dashboard(request):
    total_gas=0.000
    user_nfts=NFT.objects.filter(user=request.user).order_by('-id')
    minted=len([x for x in user_nfts if x.minted==True])
    unminted=len(user_nfts)-minted
    for i in user_nfts:
        total_gas=total_gas+ float(i.gas_fee)
    return render(request,'dashboard/home.html',{'nfts':user_nfts,'total_gas':total_gas,'unminted':unminted,'minted':minted})

def CreateNFT(request):
    if request.method=="POST":
        NFT.objects.create(
            name=request.POST['name'],
            price=request.POST['price'],
            description=request.POST['desc'],
            supply=request.POST['supply'],
            on_sale=True if request.POST['onsale']=='on' else False,
            nft_file=request.FILES['nft'],
            user=request.user
        )
        messages.success(request,"NFT created successfully")
        return redirect('dashboard')
    return render(request,'dashboard/create-nft.html')

def Withdraw(request):
    pass

def MintNFT(request,pk):
    nft=[NFT.objects.get(id=pk)]
    if request.method=="POST":
        if not request.FILES['proof']:
            messages.error(request,"Upload proof of payment")
            return render(request,'dashboard/mint-nft.html',{'nft':nft})
        else:
            MintingPayment.objects.create(
            nft=NFT.objects.get(id=pk),
            proof=request.FILES['proof']
            )
            messages.success(request,"Minting payment added, wait for confirmation")
            return redirect('dashboard')
    return render(request,'dashboard/mint-nft.html',{'nft':nft})
