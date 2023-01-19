from django.urls import path
from .views import generate_image

urlpatterns = [
    path('', generate_image, name='generate_image')
]
