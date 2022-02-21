from django.shortcuts import render
from .models import Activity


def home(request):
    activity = Activity.objects.last_6_activities()
    context = {
        'activity': activity
    }
    return render(request, 'main/home.html', context)
