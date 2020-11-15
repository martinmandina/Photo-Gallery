from django.test import TestCase
from .models import Location

# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(title = 'Mombasa')
  
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location)) 

    def test_location_save(self):
        self.location.location_save()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)
