from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from projects.models import Project
from blog.models import Article

class Site:
    domain = 'naparilidv.com'
    

class BaseSitemap(Sitemap):
    protocol = 'https' 
    
    def get_urls(self, site=None, **kwargs):
        site = Site()
        return super(BaseSitemap, self).get_urls(site=site, **kwargs)


class HomeViewSitemap(BaseSitemap): 
    priority = 1 

    def items(self): 
        return [
            'home:home',
        ]
    
    def location(self, item):
        return reverse(item)


class StaticViewSitemap(BaseSitemap):
    priority = 0.9

    def items(self):
        return [ 
            'projects:catalog', 
            'blog:blog', 
            'contacts:contacts',
            'contacts:gallery',
            'contacts:about_company',
        ]  

    def location(self, item):
        return reverse(item)
    

class ProjectViewSitemap(BaseSitemap): 
    priority = 0.8 

    def items(self): 
        return Project.objects.all()
    

class BlogViewSitemap(BaseSitemap): 
    priority = 0.7 

    def items(self): 
        return Article.objects.all()
    

class OtherStatisViewSitemap(BaseSitemap): 
    priority = 0.75  

    def items(self): 
        return [ 
            'contacts:privacy_policy', 
        ]  
    
    def location(self, item):
        return reverse(item)
