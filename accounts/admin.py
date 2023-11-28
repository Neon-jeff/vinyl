from django.contrib import admin
from .models import *
# Register your models here.



class NFTAdmin(admin.ModelAdmin):
    search_fields = ['name',]

class ProfileAdmin(admin.ModelAdmin):
    search_fields=['']

admin.site.register(UserProfile)
admin.site.register(NFT,NFTAdmin)
admin.site.register(MintingPayment)
admin.site.register(VerficationFee)
admin.site.register(MarketPlace)
admin.site.register(Withdrawal)
admin.site.register(History)
admin.site.register(OwnedNFTs)
admin.site.register(Sale)
