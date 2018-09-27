from django.db import models
import datetime as dt


# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length = 60)
    pic = models.ImageField(upload_to = 'pichazza/')
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
