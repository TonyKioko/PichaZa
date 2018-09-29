from django.test import TestCase
from .models import *

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
