from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def count_img(self):
        return self.images_gallery.count()


class Images(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='images_gallery')
    title = models.TextField()
    img = models.ImageField(upload_to='gallery/')
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title
