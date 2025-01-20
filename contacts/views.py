from django.shortcuts import render
from django.views import View 
from django.http import JsonResponse
from django.template.loader import render_to_string 
from .models import (
    PrivacyPolicy, 
    Worker,
    CertificatePhoto,
    Partner,
)
from projects.models import Category
from .forms import FeedbackForm, GalleryFilterForm
from projects.models import Project
from amocrm.services import crm


class ContactsView(View): 
    template_name = 'contacts/contacts.html'

    def get(self, request): 
        return render(request, self.template_name)
    

class GalleryView(View): 
    template_name = 'contacts/gallery.html'

    def get(self, request): 
        filter_form = GalleryFilterForm(request.GET)

        heading = 'Галерея'
        if filter_form.is_valid():
            category_id = filter_form.cleaned_data.get('category')

            if category_id:
                category = Category.objects.get(id=category_id)
                match category.name:
                    case 'Дома':
                        heading = 'Галерея домов'
                    case 'Коттеджи':
                        heading = 'Галерея коттеджей'
                    case 'Бани':
                        heading = 'Галерея бань'
                    case _:
                        heading = 'Галерея'

        context = {
            'heading': heading,
            'gallery_photos': Project.objects.filter(is_in_gallery=True),
            'filter_form': filter_form,
        }
        return render(request, self.template_name, context)
    

class AboutCompanyView(View): 
    template_name = 'contacts/about-company.html'

    def get(self, request): 
        workers = Worker.objects.all()
        certificates = CertificatePhoto.objects.all()
        partners = Partner.objects.all()
        context = {
            'workers': workers,
            'certificates': certificates,
            'partners': partners,
        }
        return render(request, self.template_name, context)
    

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
            crm.create_lead(f'Заявка с сайта | {new_request.phone}')
            return JsonResponse({'status': 'ok'}, status=200)
        return JsonResponse({'status': 'error'}, status=400)
    

class GalleryPhotosAPIView(View): 
    def get(self, request): 
        projects = Project.objects.filter(is_in_gallery=True)
        filter_form = GalleryFilterForm(request.GET)

        if filter_form.is_valid():
            cd = filter_form.cleaned_data 

            category = cd.get('category') 
            if category: 
                projects = projects.filter(category__id=category)

        rendered_gallery_projects = render_to_string('contacts/includes/gallery_slider.html', {
            'gallery_photos': projects,
        }) 
        rendered_text_slides = render_to_string('contacts/includes/gallery_text.html', {
            'gallery_photos': projects,
        })

        return JsonResponse({
            'gallery_html': rendered_gallery_projects, 
            'gallery_text': rendered_text_slides,
        })
    

class GalleryDetailsAPIView(View): 
    def get(self, request, project_id: int): 
        project = Project.objects.get(pk=project_id)

        rendered_project_details = render_to_string('contacts/includes/gallery_project.html', {
            'project': project,
        }) 

        return JsonResponse({'html': rendered_project_details})