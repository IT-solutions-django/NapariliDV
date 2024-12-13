from django.shortcuts import render
from django.views import View 


class ContactsView(View): 
    template_name = 'contacts/contacts.html'

    def get(self, request): 
        return render(request, self.template_name)
    

class GalleryView(View): 
    template_name = 'contacts/gallery.html'

    def get(self, request): 
        return render(request, self.template_name)
    

class AboutCompanyView(View): 
    template_name = 'contacts/about-company.html'

    def get(self, request): 
        return render(request, self.template_name)