from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import uuid
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import send_mail
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.

# Send Welcome Emails

def SendEmail(user):
    sender = settings.EMAIL_HOST_USER
    recipient = f'{user.email}'

# Create message
    msg = MIMEMultipart("alternative")
    email_template=render_to_string('components/transactional.html',{'user':user})

    msg['Subject'] = f"Welcome to Rarefinds"
    msg['From'] = sender
    msg['To'] = recipient
    part2 = MIMEText(email_template, 'html')
    msg.attach(part2)
# Create server object with SSL option
    server = smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT)

# Perform operations via server
    server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    server.sendmail(sender, [recipient], msg.as_string())
    server.quit()


def RegisterUser(request):
    if request.user.is_authenticated and request.method=='GET':
        return redirect('dashboard')
    elif request.method=='POST':
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
            SendEmail(user=user)
            return redirect('success')
        elif used_uname!=None:
            messages.error(request,'Username already taken')
            return render(request,'pages/register.html')
        elif used_email!=None:
            messages.error(request,"Email already taken")
            return render(request,'pages/register.html')
    return render(request,'pages/register.html')

def RegisterSuccess(request):
    return render(request,'pages/regsucess.html')

def VerifySuccess(request):
    return render(request,'pages/verifysuccess.html')
# Logs in the user

def Login(request):

    if request.user.is_authenticated:
        return redirect('dashboard')
    elif request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.filter(email=email).first()
        if user:
            auth_user=authenticate(username=user.username,password=password)
            if auth_user == None:
                messages.error(request,'Invalid Credentials, check password')
                return render(request,'pages/login.html')
            else:
                login(request, auth_user)
                return redirect('dashboard')
        else:
            messages.error(request,'No existing account')
            return render(request,'pages/login.html')
        # return redirect('home')
    return render(request,'pages/login.html')

@login_required(login_url='login')
def Dashboard(request):
    user_nfts=NFT.objects.filter(user=request.user).order_by('-id')
    minted=len([x for x in user_nfts if x.minted==True])
    sold_amt=len([x for x in user_nfts if (x.amount_sold!=None and x.amount_sold>0)])
    unminted=len(user_nfts)-minted
    total_gas='%.2f'%(unminted*0.18)
    return render(request,'dashboard/home.html',{'nfts':user_nfts,'total_gas':total_gas,'unminted':unminted,'minted':minted,'sold':sold_amt})

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
    withdrawals=Withdrawal.objects.filter(user=request.user).order_by('-created')
    if request.user.profile.can_withdraw == False:
        return redirect('upgrade')
    else:
        if request.method=="POST":
            if float(request.POST['amount'])>request.user.profile.balance:
                messages.error(request,"Amount exceeds balance, try again")
                return render(request,'dashboard/withdraw.html',{'w':withdrawals})
            else:
                Withdrawal.objects.create(
                user=request.user,
                amount=request.POST['amount']
                )
                request.user.profile.balance=float(request.user.profile.balance - float(request.POST['amount']))
                request.user.profile.save()
                messages.success(request,"Withdrawal pending,please for confirmation")
                return render(request,'dashboard/withdraw.html',{'w':withdrawals})
    return render(request,'dashboard/withdraw.html',{'w':withdrawals})

def MintNFT(request,pk):
    nft=NFT.objects.get(id=pk)
    list_nft=[NFT.objects.get(id=pk)]
    if request.method=="POST":
        if not request.FILES['proof']:
            messages.error(request,"Upload proof of payment")
            return render(request,'dashboard/mint-nft.html',{'nft':list_nft})
        else:
            MintingPayment.objects.create(
            nft=NFT.objects.get(id=pk),
            proof=request.FILES['proof']
            )
            nft.pending=True
            nft.save()
            messages.success(request,"Minting payment added, wait for confirmation")
            return redirect('dashboard')
    return render(request,'dashboard/mint-nft.html',{'nft':list_nft})

@login_required(login_url='login')
def AddWallet(request):
    if request.method=="POST":
        user=UserProfile.objects.get(user=request.user)
        user.wallet_address=request.POST['addr']
        user.save()
        messages.success(request,"Wallet Added")
        return redirect("dashboard")
    return render(request,'dashboard/add-wallet.html')

@login_required(login_url='login')
def ViewNFT(request,pk):
    nft=NFT.objects.get(id=pk)
    return render(request,'dashboard/nft-details.html',{'nft':nft})

@login_required(login_url='login')
def UpgradeAccount(request):
    if request.user.profile.can_withdraw:
        messages.error(request,"Account Upgraded created")
        return redirect('dashboard')
    elif request.method=="POST":
        VerficationFee.objects.create(
            user=request.user,
            proof=request.FILES['proof']
        )
        messages.success(request,"Account upgrade in process")
        return redirect('dashboard')
    return render(request,'dashboard/upgrade.html')


def SearcUsers(request):
    if request.method=='GET':
        users=User.objects.filter(Q(username__startswith=request.GET['search']))
        return render(request,'pages/search.html',{'users':users})

def UserDetails(request,pk):
    user=User.objects.get(id=pk)
    nfts=NFT.objects.filter(user=user,minted=True)
    return render(request,'pages/user-details.html',{'user':user,'nfts':nfts})

@login_required(login_url='login')
def UserHistory(request):
    histories=History.objects.filter(user=request.user).order_by('-created')
    return render(request,'dashboard/history.html',{"histories":histories})

@login_required(login_url='login')
def Logout(request):
    logout(request)
    return redirect('login')

def Market(request):
    market=MarketPlace.objects.all()
    nft=NFT.objects.filter(minted=True)
    return render(request,'pages/marketplace.html',{"market":market,"nfts":nft})

def Activate(request):
    profile=UserProfile.objects.filter(token=request.GET['token']).first()
    profile.verified=True
    profile.save()
    return redirect('vsuccess')

@login_required()
def UpdateAvatar(request):
    if request.method=='POST':
        request.user.profile.avatar=request.FILES['avatar']
        request.user.profile.save()
        messages.success(request,'Avatar Image Updated')
        return redirect('dashboard')
    return render(request,'dashboard/avatar.html')
