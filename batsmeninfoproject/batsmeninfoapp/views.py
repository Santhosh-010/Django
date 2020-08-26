from django.shortcuts import render
from .models import Batsmen_Info

# Create your views here.

def display_batsmen(request):
	batsmen_lst = Batsmen_Info.objects.all()#This will fetch the data from database
	return render(request,'batsmeninfoapp/display.html',{'batsmen_lst':batsmen_lst})



