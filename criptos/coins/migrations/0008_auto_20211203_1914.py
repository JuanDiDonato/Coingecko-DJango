# Generated by Django 3.2.9 on 2021-12-03 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coins', '0007_wallet_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='user',
        ),
        migrations.AddField(
            model_name='wallet',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
