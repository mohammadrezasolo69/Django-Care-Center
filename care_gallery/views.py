from django.shortcuts import render
from .models import Gallery, Images


def list_category(request):
    gallery = Gallery.objects.filter(status=True)
    images = Images.objects.filter(status=True)
    return render(request, 'gallery/gallery.html', {'Gallery': gallery, 'Images': images})
