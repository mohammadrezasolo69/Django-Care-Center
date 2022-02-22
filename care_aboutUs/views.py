from django.shortcuts import render
from .models import AboutUs


def about_us(request):
    About = AboutUs.objects.active_about()
    return render(request, 'about/about.html', {'About': About})
