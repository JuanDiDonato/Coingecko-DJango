from django.contrib import admin
from django.urls import path
from .views import index, wallet_add, WalletDelete, WalletList, register

urlpatterns = [
    path('', index, name='index'),
    path('wallet/',WalletList.as_view(),name='get_wallet'),
    path('wallet/<str:pk>',wallet_add,name='wallet_add'),
    path('wallet/<str:pk>/delete', WalletDelete.as_view(),name='delete_coin'),
    path('register/',register,name='register')
]