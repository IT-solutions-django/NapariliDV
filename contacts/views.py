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
    

class AboutView(View): 
    template_name = 'contacts/about.html'

    def get(self, request): 
        return render(request, self.template_name)