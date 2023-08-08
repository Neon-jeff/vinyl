# Generated by Django 4.2.3 on 2023-08-06 21:10

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_mintingpayment_confirmed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nft',
            name='nft_file',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
