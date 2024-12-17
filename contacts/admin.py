from django.contrib import admin
from .models import (
    Worker,
    Request, 
    GalleryPhoto,
    PrivacyPolicy, 
    PrivacyPolicyParagraph
)
from .filters import IsClosed


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin): 
    list_display = ['last_name', 'first_name']


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin): 
    list_display = ['name', 'phone', 'is_closed']
    list_filter = [
        IsClosed
    ]


@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin): 
    list_display = ['pk', 'photo']


class PrivacyPolicyParagraphInline(admin.TabularInline):
    model = PrivacyPolicyParagraph
    extra = 1  
    verbose_name = "Абзац"
    verbose_name_plural = "Абзацы"


@admin.register(PrivacyPolicy)
class ArticleAdmin(admin.ModelAdmin): 
    list_display = ['title']
    search_fields = ['title']
    inlines = [PrivacyPolicyParagraphInline]