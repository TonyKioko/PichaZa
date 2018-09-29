from django.test import TestCase
from .models import *

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(category='Food')

    def test_category_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category_method(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category_method(self):
        self.category.save_category()
        self.category.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)

class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.location= Location(location = 'Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)
    def test_delete_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.location.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)

class ImageTestClass(TestCase):
    def setUp(self):
        self.image = Image(name='kitten',pic='imageurl',description='pet')
        self.location= Location(location = 'Nairobi')
        self.location.save_location()
        self.category = Category(category='Food')
        self.category.save_category()
        self.image.location.add(self.location)
        self.image.category.add(self.category)


    def test_image_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_method(self):
        self.image.save_image()
        images  = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_image_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)
