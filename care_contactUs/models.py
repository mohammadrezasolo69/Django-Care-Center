from django.db import models


class ContactUs(models.Model):
    phone_1 = models.CharField(max_length=12)
    phone_2 = models.CharField(max_length=12)
    phone_3 = models.CharField(max_length=12)
    address_instagram = models.CharField(max_length=200,null=True)
