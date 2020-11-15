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

    @classmethod
    def location_update(cls, id, value):
        cls.objects.filter(id=id).update(title=value)


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def category_save(self):
        self.save()

    def category_delete(self):
        self.delete()

    @classmethod
    def category_update(cls, id, value):
        cls.objects.filter(id=id).update(title=value)


class Image(models.Model):
    name = models.CharField(max_length =60)
    description = models.TextField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    photos = models.ImageField(upload_to = 'images/')

    def image_save(self):
        self.save()

    def image_delete(self):
        self.delete()

    def update_image(self):
        self.update()

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_category(cls,search_term):
        categories = cls.objects.filter(category__title__icontains=search_term)
        return categories

    @classmethod
    def image_single(cls,id):
        photo = cls.objects.get(pk = id)
        return photo

    