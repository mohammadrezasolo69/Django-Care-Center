from django.db import models
from django.http import Http404


class AboutUsManager(models.Manager):
    def active_about(self):
        qs = self.get_queryset().filter(status=True).order_by('-id')
        if qs is None:
            raise Http404
        return qs.first()


class AboutUs(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    descriptions = models.TextField()
    status = models.BooleanField(default=True)

    objects = AboutUsManager()

    def __str__(self):
        return self.title
