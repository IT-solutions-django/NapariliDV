from django.urls import path
from .views import *


app_name = 'projects'


urlpatterns = [
    path('', CatalogView.as_view(), name='home'), 
]