from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def crikimgview(request):
	form = CricketerForm()
	if request.method=='POST':
		form = CricketerForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return success(request)
	return render(request,'uploadapp/display.html',{'form':form})

def success(request):
	s1 = "<center><h1>Successfully Uploaded...</h1></center>"
	return HttpResponse(s1)

def display_cricketer_img(request):
	if request.method=='GET':
		cricketers = Cricketer.objects.all()
		return render(request,'uploadapp/image.html',{'cricketers':cricketers})
