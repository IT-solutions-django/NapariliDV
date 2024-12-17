from django.shortcuts import render
from django.views import View 
from .models import (
    ArticleType, 
    Article, 
    Paragraph
)


class BlogView(View): 
    template_name = 'blog/blog.html'

    def get(self, request): 
        articles = Article.objects.all()
        context = {
            'articles': articles,
        }
        return render(request, self.template_name, context)
    

class ArticleView(View): 
    template_name = 'blog/article.html'

    def get(self, request, article_slug: str): 
        article = Article.objects.get(slug=article_slug)
        context = {
            'article': article
        }
        return render(request, self.template_name, context)