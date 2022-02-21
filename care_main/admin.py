from django.contrib import admin
from .models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'descriptions', 'logo_tag', 'status')
    list_editable = ('status',)
