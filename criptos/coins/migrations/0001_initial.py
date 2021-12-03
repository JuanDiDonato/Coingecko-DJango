# Generated by Django 3.2.9 on 2021-12-03 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('crypto', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('symbol', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('last_updated', models.DateField(max_length=100)),
            ],
        ),
    ]
