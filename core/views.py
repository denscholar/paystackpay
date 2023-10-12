from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PaymentForm
from .models import Payment
from django.conf import settings
from django.contrib import messages


def initiate_payment(request):
    payment_form = PaymentForm(request.POST)
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            return render(
                request,
                "core/make_payment.html",
                {
                    "payment": payment,
                    "paystack_public key": settings.PAYSTACK_PUBLIC_KEY,
                },
            )
    else:
        payment_form = PaymentForm()

    return render(request, "core/initiate_payment.html", {"payment_form": payment_form})


def verify_payment(request, ref: str):
    payment = get_object_or_404(Payment, pk=ref)
    verified = payment.verify_payment()

    if verified:
        messages.success(request, "verification successful")

    else:
        messages.error(request, "verification failed")
    return redirect("payment:initiate-payment")
