from django.contrib import admin
from .models import (
    Project, 
    Category, 
    Material, 
    RoofType, 
    ProjectPhoto
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin): 
    list_display = ['name']


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin): 
    list_display = ['name']


@admin.register(RoofType)
class RoofTypeAdmin(admin.ModelAdmin): 
    list_display = ['name']


class ProjectPhotoInline(admin.TabularInline): 
    model = ProjectPhoto
    extra = 0


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin): 
    list_display = ['name', 'category', 'square', 'price', 'material', 'roof_type', 'bedrooms_quantity', 'bathrooms_quantity']

    inlines = [
        ProjectPhotoInline,
    ] 