from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import CardForm, DonateForm

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

def donate(request):
	if request.method == "POST":
		form = CardForm(request.POST)
		#form.cleaned_data

		if form.is_valid():
			#stuff

			return HttpResponseRedirect('thanks/')

	else:
		form = DonateForm(auto_id=True)

		
	return render(request,'shop/donate.html', {'form': form})






	#return render(request,"shop/charge.html")



def donate_charge(request):
	stripe.api_key = "sk_test_A2LYgrlHFf4X2Xb9BnWrRvWW"




	if request.method == "POST":
		form = DonateForm(request.POST)

		if not form.is_valid():
			return HttpResonse("Charge Failure: Form Invalid")

		amount = form.cleaned_data['amount']
		#do token too? or can't being token not part of django form. hmm.


		token = request.POST['StripeToken']

		amount *= 100
		amount = int(amount)


		charge = stripe.Charge.create(
			amount=amount,
			currency="usd",
			source = token,
			description = "Donation"
		)

		print("This is charge: ", charge.id)

		return HttpResponse("Thank you for your donation. Your charge id#: " + charge.id)

	else:
		#charge lookup?
		return HttpResponse("This thing")


	