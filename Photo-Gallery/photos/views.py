from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Location,Category

# Create your views here.

def display_images(request):
    images = Image.get_images()
    return render(request,'images.html',{'images':images})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = images.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"image": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})



