from django.shortcuts import render
from .models import ContactUs


def contact_us(request):
    contact = ContactUs.objects.first()
    return render(request, 'contact/contact.html', {'contact': contact})
