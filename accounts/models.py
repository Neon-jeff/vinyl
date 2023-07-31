from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    verified=models.BooleanField(default=False)
    token=models.CharField(blank=True,null=True,max_length=300)
    avatar=models.ImageField(upload_to='profiles',blank=True,null=True)
    full_name=models.CharField(max_length=100,null=True,blank=True)
    wallet_address=models.CharField(max_length=100,null=True,blank=True)
    balance=models.DecimalField(decimal_places=3,max_digits=4,default=0.000,null=True,blank=True)

    def __str__(self):
        return self.user.username + 'profile'

class NFT(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='nft')
    name=models.CharField(max_length=50,default='')
    nft_file=CloudinaryField('file',blank=True,null=True)
    price=models.DecimalField(decimal_places=4,max_digits=10)
    minted=models.BooleanField(default=False)
    gas_fee=models.DecimalField(default=0.75,decimal_places=4,max_digits=10)
    sold=models.BooleanField(default=False)
    token=models.CharField(blank=True,null=True)
    on_sale=models.BooleanField(default=False)
    description=models.TextField(max_length=500,default='')
    supply=models.IntegerField(blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    pending=models.BooleanField(default=False,null=True,blank=True)
    amount_sold=models.IntegerField(default=0,null=True,blank=True)

    def save(self,*args,**kwargs):
        if self.minted==True:
            self.pending==False
        super(NFT, self).save(*args, **kwargs)
    def __str__(self):
        return f'{self.user.username} NFT {self.name}'

class MintingPayment(models.Model):
    nft=models.ForeignKey(NFT,on_delete=models.CASCADE,related_name='mint_payment')
    created=models.DateTimeField(auto_now_add=True)
    proof=CloudinaryField('image')

    def __str__(self):
        return f'Minting payment for {self.nft.name} from {self.nft.user.username}'

