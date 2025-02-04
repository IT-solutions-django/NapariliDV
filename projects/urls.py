from django.urls import path
from .views import *


app_name = 'projects'


urlpatterns = [
    path('catalog', CatalogView.as_view(), name='catalog'), 
    path('<slug:project_slug>/', ProjectView.as_view(), name='project'),
]