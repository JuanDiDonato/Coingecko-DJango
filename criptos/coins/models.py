from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User  

class Wallet(models.Model):
    crypto = CharField(primary_key=True, max_length=255)
    symbol = CharField(max_length=100, blank=False, null=False)
    price = CharField(max_length=100)
    last_updated = CharField(max_length=100,blank=True,null=True)
    image = CharField(max_length=255,blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta :
        ordering = ["price"]

    def __str__(self):
        return self.crypto