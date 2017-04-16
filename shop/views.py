from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import CardForm

import stripe

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

def checkout(request):
	if request.method == "POST":
		form = CardForm(request.POST)
		#form.cleaned_data

		if form.is_valid():
			#stuff

			return HttpResponseRedirect('thanks/')

	else:
		form = CardForm()

		
	return render(request,'shop/checkout.html', {'form': form})






	#return render(request,"shop/charge.html")



def checkout_charge(request):
	stripe.api_key = "sk_test_A2LYgrlHFf4X2Xb9BnWrRvWW"


	if request.method == "POST":
		#elx = request.content_params['stripeToken']
		return HttpResponse("hey work")

	else:
		return HttpResponse("This thing")


	