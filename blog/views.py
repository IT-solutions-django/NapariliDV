from django.http import JsonResponse
from django.shortcuts import render
from django.views import View 
from django.template.loader import render_to_string 
from projects.services import get_paginated_collection
from .models import (
    ArticleType, 
    Article, 
    Paragraph
)
from .forms import ArticlesForm


class BlogView(View): 
    template_name = 'blog/blog.html'

    def get(self, request): 
        articles = Article.objects.all()
        page_title = 'Новости'

        form = ArticlesForm(request.GET)

        if form.is_valid():
            cd = form.cleaned_data

            article_type = cd.get('article_type')
            if article_type:
                articles = articles.filter(article_type__id=article_type) 

        articles = get_paginated_collection(request, articles, 12)

        context = {
            'articles': articles,
            'page_title': page_title,

            'form': form,
        }
        return render(request, self.template_name, context)
    

class FilterBlogAPIView(View): 
    def get(self, request):
        articles = Article.objects.all()
        filter_form = ArticlesForm(request.GET)

        if filter_form.is_valid():
            cd = filter_form.cleaned_data

            article_type = cd.get('article_type')
            if article_type:
                articles = articles.filter(article_type__id=article_type) 

        articles = get_paginated_collection(request, articles, 12)

        rendered_articles_cards = render_to_string('blog/includes/articles_cards.html', {'articles': articles})
        rendered_pagination = render_to_string('blog/includes/pagination.html', {
            'articles': articles,
        })

        data = {
            'html': rendered_articles_cards, 
            'pagination': rendered_pagination,
        }

        return JsonResponse(data)
    

class ArticleView(View): 
    template_name = 'blog/article.html'

    def get(self, request, article_slug: str): 
        article = Article.objects.get(slug=article_slug)
        similar_articles = Article.objects.filter(article_type=article.article_type).exclude(id=article.id)[:3]
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