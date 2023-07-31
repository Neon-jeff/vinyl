from django.urls import path
from .views import *

urlpatterns = [
    path("register/",RegisterUser,name='register' ),
    path("success/",RegisterSuccess,name='success'),
    path('login/',Login,name='login'),
    path('user/dashboard',Dashboard,name='dashboard'),
    path('user/create-nft',CreateNFT,name='create-nft'),
    path('user/mint-nft/<int:pk>',MintNFT,name='mintnft'),
    path('user/addwallet/',AddWallet,name='addwallet')
]
