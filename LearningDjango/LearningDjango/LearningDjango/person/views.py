from django.shortcuts import render
from .models import *
from .forms import *

def index(request):
    form = PersonForm()
    context = {'form' : form}
    return render(request, 'person/index.html', context)