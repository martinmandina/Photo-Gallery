from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Location,Category

# Create your views here.

def display_images(request):
    images = Image.get_images()
    return render(request,'images.html',{'images':images})

def search_image(request):
    categories = Category.objects.all()
    locations = Location.objects.all()
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{'images': images, 'message': message, 'categories': categories,"locations": locations})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def image_single(request, photo_id):
    try:
        singlephoto = photos.objects.get(id=photo_id)
    except DoesNotExist:
        raise Http404()
    return render(request, 'Singleimage.html', {'singlephoto':singlephoto})




