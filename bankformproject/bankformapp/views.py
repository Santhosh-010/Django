from django.shortcuts import render
from . import forms
from django.http import HttpResponse

# Create your views here.
def accregister(request):
	form = forms.AccountRegistration()
	if request.method=='POST':
		form = forms.AccountRegistration(request.POST)
		if form.is_valid():
			form.save()
			print('Data got inserted into Database Successfully')
			return success(request)
	return render(request,'bankformapp/display.html',{'form':form})


def success(request):
	s1 = "<center><h1>Successfully Uploaded</h1></center>"
	return HttpResponse(s1)

	
