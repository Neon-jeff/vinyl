from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    verified=models.BooleanField(default=False)
    token=models.CharField(blank=True,null=True,max_length=300)
    avatar=models.ImageField(upload_to='profiles',blank=True,null=True)
    full_name=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.user.username + 'profile'
