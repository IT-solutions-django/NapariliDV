from django.urls import path
from .views import *


app_name = 'projects'


urlpatterns = [
    path('catalog', CatalogView.as_view(), name='catalog'), 
    path('<int:id>/', ProjectView.as_view(), name='project'),
]