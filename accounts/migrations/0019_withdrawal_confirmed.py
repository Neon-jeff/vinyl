# Generated by Django 4.2.3 on 2023-08-03 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_nft_gas_fee_alter_nft_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdrawal',
            name='confirmed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]