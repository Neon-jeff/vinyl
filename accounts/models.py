from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    verified=models.BooleanField(default=False)
    token=models.CharField(blank=True,null=True,max_length=300)
    avatar=models.ImageField(upload_to='profiles',blank=True,null=True)
    full_name=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.user.username + 'profile'

class NFT(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='nft')
    name=models.CharField(max_length=50,default='')
    image=models.ImageField(upload_to='nfts',blank=True,null=True)
    price=models.DecimalField(decimal_places=4,max_digits=10)
    minted=models.BooleanField(default=False)
    gas_fee=models.DecimalField(default=0.75,decimal_places=4,max_digits=10)

    def __str__(self):
        return f'{user.username} NFT'
