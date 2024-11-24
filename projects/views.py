from django.shortcuts import render
from django.views import View 
from .models import (
    Project, 
    Category, 
    Material, 
    RoofType, 
)


class CatalogView(View): 
    template_name = 'projects/catalog.html'

    def get(self, request): 
        projects = Project.objects.all() 
        categories = Category.objects.all()
        materials = Material.objects.all()
        roof_types = RoofType.objects.all()
        context = {
            'projects': projects
        }
        return render(request, self.template_name, context)