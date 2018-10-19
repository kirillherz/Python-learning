from django.forms import ModelForm
from LearningDjango.person.models import *

class PersonForm(ModelForm):
    
    class Meta:
        model = Person
        exclude = ['id']
        

