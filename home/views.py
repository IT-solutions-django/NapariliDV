from django.shortcuts import render
from django.views import View 
from projects.models import Project


class HomeView(View): 
    template_name = 'home/home.html'

    def get(self, request): 
        context = {
            'best_projects': Project.objects.all(),
        }
        return render(request, self.template_name, context)

