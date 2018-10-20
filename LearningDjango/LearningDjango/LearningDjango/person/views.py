from django.shortcuts import render
from .models import *
from .forms import *

def index(request):

    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            template = 'person/save.html'
        else:
           form = PersonForm()
           template = 'person/index.html'
    else:
        template = 'person/index.html'
        form = PersonForm() 
    context = {'form' : form}
    return render(request, template, context)