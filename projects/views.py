from django.shortcuts import render
from django.views import View 
from .models import (
    Project, 
    Category, 
    Material, 
    RoofType, 
)
from .forms import CatalogFiltersForm


class CatalogView(View): 
    template_name = 'projects/catalog.html'

    def get(self, request): 
        projects = Project.objects.all() 
        form = CatalogFiltersForm(request.GET)

        if form.is_valid():
            cd = form.cleaned_data
            projects = Project.objects.all()
            
            selected_categories = cd.get('categories')
            if selected_categories:
                projects = projects.filter(category__id__in=selected_categories)

            selected_materials = cd.get('materials')
            if selected_materials:
                projects = projects.filter(material__id__in=selected_materials)

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


        context = {
            'form': form,
            'projects': projects
        }
        return render(request, self.template_name, context)