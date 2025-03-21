"""
URL configuration for NapariliDV project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings
from django.urls import re_path
from django.views.static import serve
from django.contrib.sitemaps.views import sitemap
from .sitemaps import (
    HomeViewSitemap,
    StaticViewSitemap, 
    OtherStatisViewSitemap,
    ProjectViewSitemap, 
    BlogViewSitemap,
)

from home.views import handler404


sitemaps = {
    'home': HomeViewSitemap,
    'static': StaticViewSitemap,
    'other_static': OtherStatisViewSitemap,
    'projects': ProjectViewSitemap,
    'blog': BlogViewSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('home.urls', namespace='home')),
    path('projects/', include('projects.urls', namespace='projects')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('contacts/', include('contacts.urls', namespace='contacts')),

    path('not-found/', handler404, name='not-found'),

    re_path(r'^robots\.txt$', serve, {
        'document_root': settings.BASE_DIR,
        'path': 'robots.txt',
    }),
    
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
)
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'home.views.handler404'