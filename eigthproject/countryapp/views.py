from django.shortcuts import render

# Create your views here.
def switzerland(request):
	msg = 'WORKS IN SWITZERLAND'
	my_dict = {'msg':msg}
	return render(request,'countryapp/display.html',context=my_dict)


def newzeland(request):
	msg = 'WORKS IN NEWZELAND'
	my_dict = {'msg':msg}
	return render(request,'countryapp/display.html',context=my_dict)