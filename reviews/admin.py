from django.contrib import admin
from .models import (
    Review,
    Platform
)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin): 
    list_display = ['id', 'username', 'content', 'created_at']


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin): 
    list_display = ['name']