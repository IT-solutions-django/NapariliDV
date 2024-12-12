from django.shortcuts import render
from django.views import View 



class BlogView(View): 
    template_name = 'blog/blog.html'

    def get(self, request): 
        return render(request, self.template_name)