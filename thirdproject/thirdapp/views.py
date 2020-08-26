from django.shortcuts import render
from datetime import datetime

# Create your views here.
def greet_django(request):
	msg = "Good Morning"
	date = datetime.now()

	my_dict = {'msg':msg,'date':date}

	return render(request,'thirdapp/display.html',context=my_dict)
