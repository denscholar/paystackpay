from django.shortcuts import render
from .models import Payment
from django.conf import settings

def initiate_payment(request):
	if request.method == "POST":
		amount = request.POST['amount']
		email = request.POST['email']

		pk = settings.PAYSTACK_PUBLIC_KEY

		payment = Payment.objects.create(amount=amount, email=email)
		payment.save()

		context = {
			'payment': payment,
			'field_values': request.POST,
			'paystack_pub_key': pk,
			'amount_value': payment.amount_value(),
		}
		return render(request, 'core/make_payment.html', context)

	return render(request, 'core/payment.html')


def verify_payment(request, ref):
	payment = Payment.objects.get(ref=ref)
	verified = payment.verify_payment()

	if verified:
		print(" funded wallet successfully")
		return render(request, "core/success.html")
	return render(request, "core/success.html")