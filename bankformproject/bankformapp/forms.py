from django import forms
from bankformapp.models import AccDetails

'''
class AccountRegistration(forms.Form):
    # TODO: Define form fields here
    FirstName = forms.CharField()
    LastName = forms.CharField()
    DOB = forms.DateField()
    Address = forms.CharField()
    AccType = forms.CharField()
    PanNo = forms.CharField()'''

class AccountRegistration(forms.ModelForm):
    # TODO: Define form fields here
    class Meta:
    	model = AccDetails
    	fields = '__all__'
    

    



