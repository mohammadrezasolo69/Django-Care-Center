from django.contrib import admin
from .models import Gallery, Images


@admin.register(Images)
class ImgGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'gallery', 'status')
    list_filter = ('gallery', 'status')
    list_editable = ('status',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'count_img')
    list_editable = ('status',)
