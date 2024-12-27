from django.http import JsonResponse
from django.shortcuts import render
from django.views import View 
from django.template.loader import render_to_string 
from projects.services import get_paginated_collection
from .models import ( 
    Article, 
    Paragraph
)


class BlogView(View): 
    template_name = 'blog/blog.html'

    def get(self, request): 
        articles = Article.objects.all()

        articles = get_paginated_collection(request, articles, 12)

        context = {
            'articles': articles,
        }
        return render(request, self.template_name, context)
    

class ArticleView(View): 
    template_name = 'blog/article.html'

    def get(self, request, article_slug: str): 
        article = Article.objects.get(slug=article_slug)
        similar_articles = Article.objects.all().exclude(pk=article.pk)[:3]
        try:
            previous_article = article.get_previous_by_created_at()
        except Article.DoesNotExist:
            previous_article = None
        try:
            next_article = article.get_next_by_created_at()
        except Article.DoesNotExist:
            next_article = None
        context = {
            'article': article, 
            'similar_articles': similar_articles,
            'previous_article': previous_article,
            'next_article': next_article,
        }
        return render(request, self.template_name, context)