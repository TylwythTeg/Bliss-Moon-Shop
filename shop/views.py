from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import CardForm

# Create your views here.

def index(request):
	#return HttpResponse("Hey")
	return render(request,"shop/index.html")

def charge(request):
	if request.method == "POST":
		form = CardForm(request.POST)
		#form.cleaned_data

		if form.is_valid():
			#stuff

			return HttpResponseRedirect('thanks/')

	else:
		form = CardForm()

		
	return render(request,'shop/charge.html', {'form': form})






	#return render(request,"shop/charge.html")
	