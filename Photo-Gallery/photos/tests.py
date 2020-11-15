from django.test import TestCase
from .models import Location

# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(title = 'Mombasa')
        self.location.save()
  
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location)) 

    def test_location_save(self):
        self.location.location_save()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_location_delete(self):
        self.location.location_delete()
        location = Location.objects.all()
        self.assertTrue(len(location)==0)

class CategoryTestClass(TestCase):
    def setup(self):
        self.category = Category(title = 'nature')
        self.category.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category)) 

        


    

