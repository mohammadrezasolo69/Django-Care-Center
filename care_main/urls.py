from django.urls import path
from . import views

app_name = 'care_main'
urlpatterns = [
    path('', views.home, name='home'),
]
