from django.urls import path
from .views import *


app_name = 'contacts'


urlpatterns = [
    path('', ContactsView.as_view(), name='contacts'), 
    path('gallery/', GalleryView.as_view(), name='gallery'), 
    path('about/', AboutView.as_view(), name='about'),
]