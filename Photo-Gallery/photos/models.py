from django.db import models

# Create your models here.
class Location(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def location_save(self):
        self.save()

    def location_delete(self):
        self.delete()

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    

