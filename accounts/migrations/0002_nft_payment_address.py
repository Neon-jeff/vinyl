# Generated by Django 4.2.3 on 2023-11-16 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nft',
            name='payment_address',
            field=models.CharField(default='0x3E76a9C164214721C99Be1694AFeDDe77Dd4239e', max_length=50, null=True),
        ),
    ]