# Generated by Django 3.2.9 on 2021-12-03 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0005_wallet_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='last_updated',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
