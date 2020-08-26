from django.shortcuts import render

# Create your views here.

def uc_1(request):
	msg = "JAVA AND TESTING"
	my_dict = {'msg':msg}
	return render(request,'courseapp/display.html',context=my_dict)

def uc_2(request):
	msg = "JAVA AND PYTHON"
	my_dict = {'msg':msg}
	return render(request,'courseapp/display.html',context=my_dict)

def uc_3(request):
	msg = "JAVA PYTHON AND TESTING"
	my_dict = {'msg':msg}
	return render(request,'courseapp/display.html',context=my_dict)
