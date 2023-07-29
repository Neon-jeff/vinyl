# Generated by Django 4.2.3 on 2023-07-28 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_nft_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='nft',
            name='description',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='nft',
            name='on_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='wallet_address',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='nft',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='nfts'),
        ),
    ]