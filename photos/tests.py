from django.test import TestCase
from .models import Location,Category,Image

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

    
    def test_location_update(self):
        new_location_name = 'Nairobi'
        self.location.location_update(self.location.id,new_location_name)
        location_updated = Location.objects.filter(title='Nairobi')
        self.assertTrue(len(location_updated)>0)

    

    def test_location_delete(self):
        self.location.location_delete()
        location = Location.objects.all()
        self.assertTrue(len(location)==0)

      
class CategoryTestClass(TestCase):
    def setup(self):
        self.category = Category(title = 'nature')
        self.category.save()

    def test_instance(self):
        self.category = Category(title = 'nature')
        self.category.save()
        self.assertTrue(isinstance(self.category,Category)) 

    def test_category_save(self):
        self.category = Category(title = 'nature')
        self.category.save()
        self.category.category_save()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)

    def test_category_update(self):
        self.category = Category(title = 'nature')
        self.category.save()
        new_category_title = 'Planes'
        self.category.category_update(self.category.id,new_category_title)
        category_updated = Category.objects.filter(title='Planes')
        self.assertTrue(len(category_updated)>0)

    
    def test_delete_category(self):
        self.category = Category(title = 'nature')
        self.category.save()
        self.category.category_delete()
        category = Category.objects.all()
        self.assertTrue(len(category)==0)

class ImageTestClass(TestCase):
    def setUp(self):
        self.location = Location(title='Mombasa')
        self.location.save()

        self.category = Category(title='nature')
        self.category.save()

        self.savannah = Image(name='savannah',description='green and beatiful',location=self.location,category=self.category)
        self.savannah.image_save()

    
    def test_instance(self):
        self.assertTrue(isinstance(self.savannah,Image))

    def test_image_save(self):
        self.savannah.image_save()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    # def test_image_update(self):
    #     self.savannah = Image(name='savannah',description='green and beatiful',location=self.location,category=self.category)
    #     self.savannah.image_save()
    #     self.savannah.update_image(self.savannah.id,'media/image.jpg')
    #     image_updated = Image.objects.filter(photos='media/image.jpg')
    #     self.assertTrue(len(image_updated)>0)

    def test_delete_image(self):
        self.savannah.image_save()
        self.savannah.image_delete()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)






      

    

    

    

        


    

