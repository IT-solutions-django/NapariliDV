from django.shortcuts import render
from django.views import View 
from projects.models import Project
from home.models import Slide


class HomeView(View): 
    template_name = 'home/home.html'

    def get(self, request): 
        best_projects = Project.objects.all()
        slides = Slide.objects.all()
        context = {
            'slides': slides,
            'best_projects': best_projects,
        }
        return render(request, self.template_name, context)

