from . import views
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

urlpatterns=[
    path('',views.display_images,name='photos'),
    # path('photo/(\d+)',views.image_one, name='singleimage'),
]
