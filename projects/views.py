from django.shortcuts import render
from django.views import View 
from .models import (
    Project,
)
from .services import get_paginated_collection
import random
from .forms import CatalogFiltersForm


class CatalogView(View): 
    template_name = 'projects/catalog.html'

    def get(self, request): 
        projects = Project.objects.all() 
        form = CatalogFiltersForm(request.GET)

        if form.is_valid():
            cd = form.cleaned_data
            
            selected_categories = cd.get('categories')
            if selected_categories:
                projects = projects.filter(category__id__in=selected_categories)

            selected_materials = cd.get('materials')
            if selected_materials:
                projects = projects.filter(material__id=selected_materials)

            selected_roof_types = cd.get('roof_types')
            if selected_roof_types:
                projects = projects.filter(roof_type__id=selected_roof_types)

            price_min = cd.get('price_min')
            if price_min is not None:
                projects = projects.filter(price__gte=price_min)

            price_max = cd.get('price_max')
            if price_max is not None:
                projects = projects.filter(price__lte=price_max)

            square_min = cd.get('square_min')
            if square_min is not None:
                projects = projects.filter(square__gte=square_min)

            square_max = cd.get('square_max')
            if square_max is not None:
                projects = projects.filter(square__lte=square_max)

            floors_quantity = cd.get('floors_quantity')
            if floors_quantity:
                projects = projects.filter(floors_quantity=floors_quantity)

            bedrooms_quantity = cd.get('bedrooms_quantity')
            if bedrooms_quantity:
                projects = projects.filter(bedrooms_quantity=bedrooms_quantity)

            bathrooms_quantity = cd.get('bathrooms_quantity')
            if bathrooms_quantity:
                projects = projects.filter(bathrooms_quantity=bathrooms_quantity)
            
        projects = get_paginated_collection(request, projects, 2)

        context = {
            'form': form,
            'projects': projects,
        }

        return render(request, self.template_name, context)

    

class ProjectView(View): 
    template_name = 'projects/project.html'
    
    def get(self, request, id: int): 
        project = Project.objects.get(pk=id) 
        similar_projects = random.choices(Project.objects.all(), k=5)
        context = {
            'project': project,
            'similar_projects': similar_projects,
        }
        return render(request, self.template_name, context)