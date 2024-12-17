from django.urls import path
from .views import *


app_name = 'home'


urlpatterns = [
    path('', HomeView.as_view(), name='home'), 

    path('api/best-projects-filter/', BestProjectsFilterAPIView.as_view(), name='best_projects_filter'),
]