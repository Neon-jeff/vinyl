from .models import *
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver


@receiver(post_save,sender=NFT)
def CreateNFTNotification(sender,instance,created,**kwargs):
    if created:
        History.objects.create(
            title="NFT Created",
            details=f' Hi, your NFT item {instance.name} was created with a supply of {instance.supply} copies, price for each {instance.price}',
            user=instance.user
        )
@receiver(post_save,sender=NFT)
def UpdateNFTNotification(sender,instance,created,**kwargs):
    if created == False:
        update_fields=kwargs.get('update_fields') or set()
        if 'amount_sold' in update_fields and update_fields!=None:
            History.objects.create(
                title="NFT Sold",
                details=f"Hey creator, your {instance.name} NFT has sold {instance.amount_sold} items",
                user=instance.user
            )
        if instance.amount_sold == instance.supply:
            History.objects.create(
                title="NFT Item Sold Out",
                details=f'Hey creator your {instance.name} NFT has been completely sold out',
                user=instance.user
            )
        if instance.minted ==True:
            History.objects.create(
                title="NFT Listed",
                details=f'Hey creator, your NFT {instance.name} has been listed on our marketplace',
                user=instance.user
            )

# @receiver(pre_save,sender=NFT)
# def UpdateBalance(sender,instance,created,**kwargs):
#     if created == False:
#         old_amount=NFT.objects.get(id=instance.id).amount_sold
#         self.user.profile.balance=instance.user.profile.balance + (instance.amount_sold-old_amount)*instance.price
#         instance.user.profile.save()

