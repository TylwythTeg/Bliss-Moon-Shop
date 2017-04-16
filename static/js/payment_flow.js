var stripe = Stripe('pk_test_AUCnsXVFWf8ZDIW08wvC6LR6');

var elements = stripe.elements();

var style = {
	base: {
		fontSize: '16px',
		lineHeight: '24px',
	}
};


//Card form error event handler
function errorHandler(event) {
	var displayError = document.getElementById('card-errors');

	if (event.error) {
		displayError.textContent = event.error.message;
	}
	else {
		displayError.textContent = '';
	}


}




//var card = elements.create('card', {style: style});

var cardNumber = elements.create('cardNumber', {style: style});
var cardExpiry = elements.create('cardExpiry', {style: style});
var cardCvc = elements.create('cardCvc', {style: style});
var postalCode = elements.create('postalCode', {style: style});


cardNumber.mount('#card-number');
cardExpiry.mount('#card-expiry');
cardCvc.mount('#card-cvc');
postalCode.mount('#postal-code');






//input validation error handlers
cardNumber.addEventListener('change', function (event) {
	errorHandler(event);
});

cardExpiry.addEventListener('change', function (event) {
	errorHandler(event);
});

cardCvc.addEventListener('change', function (event) {
	errorHandler(event);
});

postalCode.addEventListener('change', function (event) {
	errorHandler(event);
});


function stripeTokenHandler(token) {
	//Insert the token ID into the form so it gets submitted to the server
	var form = document.getElementById('payment-form');

	//<input type="hidden" name="stripeToken" value=token.id>
	var hiddenInput = document.createElement('input');
	hiddenInput.setAttribute('type', 'hidden');
	hiddenInput.setAttribute('name', 'StripeToken');
	hiddenInput.setAttribute('value', token.id);
	form.appendChild(hiddenInput);


	//document.write(token.id);
	//document.write(token.card.exp_month);



	form.submit();



}


function getPromise(result) {
	if (result.error) {
		//Inform the user if there was an error
		var errorElement = document.getElementbyId('card-errors');
		errorElement.textContent = result.error.message;
	}
	else {
		//send the token to server
		stripeTokenHandler(result.token);
	}
}





//Submit listener
function submitListener(event) {
	event.preventDefault();


	stripe.createToken(cardNumber).then(function(result) {
		getPromise(result);
	});

}



var form = document.getElementById('payment-form');








form.addEventListener('submit', function(event) {
	submitListener(event);
})

