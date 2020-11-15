from django.test import TestCase
from .models import Location

# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(title = 'Mombasa')
  

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))   
