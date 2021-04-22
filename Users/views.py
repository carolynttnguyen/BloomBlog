from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    form = loginForm()
    form2 = registrationForm()
    context = {
        'logForm': form,
        'regForm': form2
    }
    return render(request, 'index.html', context)

def register(request):
    pass