from . import views
from django.conf import settings
from django.urls import path,re_path
from django.conf.urls.static import static

urlpatterns=[
    path('',views.display_photos,name='photos'),
    
]