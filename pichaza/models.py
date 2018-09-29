from django.db import models
import datetime as dt


# Create your models here.
#
class Category(models.Model):
    name = models.CharField(max_length =20,default='Travel')

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
    def __str__(self):
        return self.category
    @classmethod
    def search_by_category(cls, search_term):
        images = cls.objects.filter(name__icontains=search_term)
        return images

class Location(models.Model):
    name = models.CharField(max_length=20,default="Nairobi")

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    @classmethod
    def get_location(cls, id):
        locations = Location.objects.get(pk = id)
        return locations
    def __str__(self):
        return self.location

class Image(models.Model):
    name = models.CharField(max_length = 60)
    pic = models.ImageField(upload_to = 'pichazza/', default='NO IMAGE')
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    location = models.ManyToManyField(Location)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()
    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id= id).all()
        return image

    def delete_image(self):
        self.delete()

    @classmethod
    def get_images(cls):
        images = Image.objects.all()
        return images
    @classmethod
    def search_by_category(cls,search_term):
        images_in_category = cls.objects.filter(category__category__icontains=search_term)
        return images_in_category
    @classmethod
    def filter_by_location(cls,id):
        images_location = Image.objects.filter(id=location.id)
        return images_location
