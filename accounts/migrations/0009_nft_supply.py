# Generated by Django 4.2.3 on 2023-07-29 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_nft_image_nft_nft_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='nft',
            name='supply',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
