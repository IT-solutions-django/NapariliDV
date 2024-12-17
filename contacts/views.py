from django.shortcuts import render
from django.views import View 
from django.http import JsonResponse
from .models import (
    GalleryPhoto,
    PrivacyPolicy
)
from .forms import FeedbackForm


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
    

class PrivacyPolicyView(View): 
    template_name = 'contacts/privacy_policy.html'

    def get(self, request): 
        privacy_policy = PrivacyPolicy.get_instance()
        context = {
            'privacy_policy': privacy_policy,
        }
        return render(request, self.template_name, context)
    

class SaveRequestView(View): 
    def post(self, request): 
        form: FeedbackForm = FeedbackForm(request.POST) 
        if form.is_valid(): 
            new_request = form.save() 
            return JsonResponse({'status': 'ok'}, status=200)
        return JsonResponse({'status': 'error'}, status=400)