from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # My URL
    path('', include('care_main.urls')),
    path('gallery/', include('care_gallery.urls')),
    path('about-us/', include('care_aboutUs.urls')),
    path('contact-us/', include('care_contactUs.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
