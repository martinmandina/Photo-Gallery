from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Location,Category
from django import template

def display_images(request):
    images = Image.get_images()
    return render(request,'all_images.html',{'mapicha':images})

def search_image(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_category(search_term)

        message = f"{search_term}"

        return render(request, 'search.html',{"message":message, "images": searched_images})

    else:
        message ="Search not found"

        return render(request,'search.html',{"message":message})

def image_single(request, photo_id):
    try:
        singlephoto = photos.objects.get(id=photo_id)
    except DoesNotExist:
        raise Http404()
    return render(request, 'single_image.html', {'singlephoto':singlephoto})




