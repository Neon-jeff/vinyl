# Generated by Django 4.2.3 on 2023-07-30 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_nft_created_mintingpayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='nft',
            name='pending',
            field=models.BooleanField(default=False),
        ),
    ]