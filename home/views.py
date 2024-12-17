from django.shortcuts import render
from django.views import View 
from projects.models import Project
from home.models import Slide, PopularQuestion
from contacts.models import Worker, GalleryPhoto
from projects.forms import CatalogFiltersForm
from projects.services import get_paginated_collection
from contacts.forms import FeedbackForm


class HomeView(View): 
    template_name = 'home/home.html'

    def get(self, request): 
        best_projects = Project.objects.all()
        slides = Slide.objects.all()
        workers = Worker.objects.all()
        gallery_photos = GalleryPhoto.objects.all()
        popular_questions = PopularQuestion.objects.all()
        filter_form = CatalogFiltersForm(request.GET)
        feedback_form = FeedbackForm()

        if filter_form.is_valid():
            cd = filter_form.cleaned_data
            
            selected_categories = cd.get('categories')
            if selected_categories:
                best_projects = best_projects.filter(category__id__in=selected_categories)

            selected_materials = cd.get('materials')
            if selected_materials:
                best_projects = best_projects.filter(material__id=selected_materials)

            selected_roof_types = cd.get('roof_types')
            if selected_roof_types:
                best_projects = best_projects.filter(roof_type__id=selected_roof_types)

            price_min = cd.get('price_min')
            if price_min is not None:
                best_projects = best_projects.filter(price__gte=price_min)

            price_max = cd.get('price_max')
            if price_max is not None:
                best_projects = best_projects.filter(price__lte=price_max)

            square_min = cd.get('square_min')
            if square_min is not None:
                best_projects = best_projects.filter(square__gte=square_min)

            square_max = cd.get('square_max')
            if square_max is not None:
                best_projects = best_projects.filter(square__lte=square_max)

            floors_quantity = cd.get('floors_quantity')
            if floors_quantity:
                best_projects = best_projects.filter(floors_quantity=floors_quantity)

            bedrooms_quantity = cd.get('bedrooms_quantity')
            if bedrooms_quantity:
                best_projects = best_projects.filter(bedrooms_quantity=bedrooms_quantity)

            bathrooms_quantity = cd.get('bathrooms_quantity')
            if bathrooms_quantity:
                best_projects = best_projects.filter(bathrooms_quantity=bathrooms_quantity)
            
        best_projects = get_paginated_collection(request, best_projects, 12)

        context = {
            'slides': slides,
            'best_projects': best_projects,
            'workers': workers,
            'gallery_photos': gallery_photos,
            'popular_questions': popular_questions,
            'filter_form': filter_form,
            'feedback_form': feedback_form,
        }
        return render(request, self.template_name, context)

