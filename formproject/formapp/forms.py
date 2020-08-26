from django import forms 
class StudentRegistration(forms.Form):
    # TODO: Define form fields here
    Name = forms.CharField()
    Marks = forms.IntegerField()
