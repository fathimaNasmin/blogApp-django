from django.shortcuts import render
from .forms import SubscribeForm

# Create your views here.

def subscribe(request):
    form = SubscribeForm()
    pass
