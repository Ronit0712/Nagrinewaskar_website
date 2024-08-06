from django.db import models

# Create your models here.
class ContactlistModel (models.Model):
    fullname = models.CharField(max_length = 200)
    mnumber = models.CharField(max_length = 12)
    email = models.EmailField()
    city = models.CharField(max_length = 200)
    message = models.TextField()

class InquiryModel(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)
    address = models.TextField()
    email = models.EmailField()
    message = models.TextField()