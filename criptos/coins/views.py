from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt  # Exime la vista del token
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm

from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

from .models import Wallet
from .forms import WalletForm, UserForm

# Función vista para la página inicio del sitio.
def index(request):
    coins = cg.get_coins_list()
    page = request.GET.get("page", 1)
    # Paginacion
    paginator = Paginator(coins, 40)
    try:
        coins = paginator.page(page)
    except PageNotAnInteger:
        coins = paginator.page(1)
    except EmptyPage:
        coins = paginator.page(paginator.num_pages)
    return render(request,'index.html',{'coins':coins})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Users')
            user.groups.add(group)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'auth/user_form.html',{'form':form})

@login_required
def wallet_add(request, pk):
    coin = cg.get_coins_markets(vs_currency='usd',ids=pk)
    data = {'price':coin[0]['current_price'], 'symbol':coin[0]['symbol'],'crypto':pk,'image':coin[0]['image'],'last_updated':coin[0]['last_updated'],'user':request.user}
    form = WalletForm(data)
    if form.is_valid(): 
        form.save()
    return redirect('get_wallet')

"""
--Vista de funcion--
def get_wallet(request):
    wallet = Wallet.objects.all()
    context = {'wallet':wallet}
    return render(request,'wallet/wallet.html',context)
"""

class WalletList(LoginRequiredMixin, ListView):
    model = Wallet

"""
--Vista de funcion--
def delete_coin(request, pk):
    coin = Wallet.objects.get(crypto = pk)
    coin.delete()
    return redirect('get_wallet')

"""
class WalletDelete(LoginRequiredMixin,DeleteView):
    model = Wallet
    success_url = reverse_lazy('get_wallet')
