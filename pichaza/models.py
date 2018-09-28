from django.db import models
import datetime as dt


# Create your models here.
#
class Category(models.Model):
    category = models.CharField(max_length =20,null=True)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
    def __str__(self):
        return self.category

class Location(models.Model):
    location = models.CharField(max_length=20,null=True)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    def __str__(self):
        return self.location
    @classmethod
    def search_by_category(cls, search_term):
        images = cls.objects.filter(name__icontains=search_term)
        return images

#     @classmethod
#     def search_by_location(cls, search_term):
#         images = cls.objects.filter(location__icontains=search_term)
#         return images
#     def __str__(self):
#             return self.location

class Image(models.Model):
    name = models.CharField(max_length = 60)
    pic = models.ImageField(upload_to = 'pichazza/', default='NO IMAGE')
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)



    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_images(cls):
        images = Image.objects.all()
        return images
