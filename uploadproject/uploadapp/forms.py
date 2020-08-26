from django import forms
from .models import *

class CricketerForm(forms.ModelForm):
    # TODO: Define form fields here

    class Meta:
    	model = Cricketer
    	fields = '__all__'
    