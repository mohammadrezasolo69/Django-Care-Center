from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html


class ActivityManager(models.Manager):
    def last_6_activities(self):
        qs = self.get_queryset().filter(status=True).order_by('-id')[:6]
        if len(qs) == 6 or len(qs) < 6:
            return qs
        else:
            return self.get_queryset().filter(status=True).order_by('-id')


class Activity(models.Model):
    title = models.CharField(_('عنوان'), max_length=30)
    descriptions = models.TextField(_('توضیحات'))
    logo = models.ImageField(_('لوگو'), upload_to='img/')
    status = models.BooleanField(_('نشان داده شود/نشود؟'), default=True)

    objects = ActivityManager()

    def __str__(self):
        return self.title

    def logo_tag(self):
        return format_html(
            '<img  style="border-radius: 20px;width: 100px;height: 50px" src="{}">'.format(self.logo.url))
