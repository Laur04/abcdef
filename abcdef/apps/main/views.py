from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Key

def index(request):
    return render(request, 'index.html')

def add(request, key):
    Key.objects.create(value=key)
    return redirect(reverse('index'))
