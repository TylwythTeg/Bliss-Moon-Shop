from django import forms


#Deprecated due to PCI compliance concerns
class CardForm(forms.Form):

	card_number = forms.IntegerField(label = "Card Number")
	expiration_month = forms.IntegerField(label = "Expiration Month", min_value = 1, max_value=12)
	expiration_year = forms.IntegerField(label = "Expiration Year", min_value = 1970, max_value=3000)
	cvc = forms.IntegerField(label = "CVC", min_value = 0, max_value = 9999)
	zip = forms.CharField(label = "Zip Code", max_length = 40)


class DonateForm(forms.Form):
	amount = forms.FloatField(label = "Amount",
		widget=forms.TextInput(attrs={'placeholder': 'Amount'})	
	)