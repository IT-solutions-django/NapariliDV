from django.contrib import admin
from .models import (
    Review,
    Platform, 
    ReviewPhoto,
)


class ReviewPhotoInline(admin.TabularInline):
    model = ReviewPhoto
    extra = 1  
    verbose_name = "Фото"
    verbose_name_plural = "Фото"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin): 
    list_display = ['id', 'author', 'content', 'created_at', 'platform', 'rate']
    inlines = [ReviewPhotoInline]


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin): 
    list_display = ['name']