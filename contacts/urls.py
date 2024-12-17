from django.urls import path
from .views import *


app_name = 'contacts'


urlpatterns = [
    path('', ContactsView.as_view(), name='contacts'), 
    path('gallery/', GalleryView.as_view(), name='gallery'), 
    path('about/', AboutCompanyView.as_view(), name='about_company'),
    path('privacy_policy/', PrivacyPolicyView.as_view(), name='privacy_policy'),

    path('api/save-request/', SaveRequestView.as_view(), name='save_request'),
]