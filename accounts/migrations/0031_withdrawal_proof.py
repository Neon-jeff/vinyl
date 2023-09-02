# Generated by Django 4.2.3 on 2023-08-22 14:13

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_alter_mintingpayment_nft_alter_mintingpayment_proof'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdrawal',
            name='proof',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]