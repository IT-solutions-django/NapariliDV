from django.shortcuts import render
from django.views import View 
from .models import (
    GalleryPhoto,
)


class ContactsView(View): 
    template_name = 'contacts/contacts.html'

    def get(self, request): 
        return render(request, self.template_name)
    

class GalleryView(View): 
    template_name = 'contacts/gallery.html'

    def get(self, request): 
        context = {
            'gallery_photos': GalleryPhoto.objects.all(),
        }
        return render(request, self.template_name, context)
    

class AboutCompanyView(View): 
    template_name = 'contacts/about-company.html'

    def get(self, request): 
        return render(request, self.template_name)