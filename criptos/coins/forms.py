from django import forms
from django.forms import fields
from .models import Wallet
from django.contrib.auth.models import User  

class WalletForm(forms.ModelForm):
    class Meta : 
        model = Wallet
        fields = '__all__' 

class UserForm(forms.ModelForm):
    class Meta :
        model = User
        fields = ('username', 'email', 'password')
