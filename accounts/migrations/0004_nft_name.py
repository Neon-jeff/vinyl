# Generated by Django 4.2.3 on 2023-07-27 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_userprofile_user_nft'),
    ]

    operations = [
        migrations.AddField(
            model_name='nft',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
