# Generated by Django 4.2.3 on 2023-08-18 11:01

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_remove_nft_price_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mintingpayment',
            name='nft',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mint_payment', to='accounts.nft'),
        ),
        migrations.AlterField(
            model_name='mintingpayment',
            name='proof',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]