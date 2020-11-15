from . import views
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

urlpatterns=[
    path('',views.display_images,name='photos'),
    path('search/', views.search_image,name='search_results'),
    path('photo/(\d+)',views.image_single, name='image'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
