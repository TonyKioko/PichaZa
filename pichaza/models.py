from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length = 60)
    pic = models.ImageField(upload_to = 'pichazza/')
    description = models.TextField()
