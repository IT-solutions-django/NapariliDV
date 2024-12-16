from django.shortcuts import render
from django.views import View 
from projects.models import Project
from home.models import Slide, PopularQuestion
from contacts.models import Worker, GalleryPhoto


class HomeView(View): 
    template_name = 'home/home.html'

    def get(self, request): 
        best_projects = Project.objects.all()
        slides = Slide.objects.all()
        workers = Worker.objects.all()
        gallery_photos = GalleryPhoto.objects.all()
        popular_questions = PopularQuestion.objects.all()
        context = {
            'slides': slides,
            'best_projects': best_projects,
            'workers': workers,
            'gallery_photos': gallery_photos,
            'popular_questions': popular_questions,
        }
        return render(request, self.template_name, context)

