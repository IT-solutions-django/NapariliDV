from django.contrib import admin
from .models import (
    Project, 
    Category, 
    Material, 
    RoofType, 
    ProjectPhoto, 
    Layout,
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


@admin.register(Layout)
class LayoutAdmin(admin.ModelAdmin): 
    list_display = ['name']


class ProjectPhotoInline(admin.TabularInline): 
    model = ProjectPhoto
    extra = 0


class LayoutInline(admin.TabularInline): 
    model = Layout 
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin): 
    list_display = ['name', 'category', 'square', 'price', 'material', 'roof_type', 'bedrooms_quantity', 'bathrooms_quantity']
    list_filter = ['category', 'material', 'roof_type', 'is_in_gallery']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


    inlines = [
        ProjectPhotoInline,
        LayoutInline,
    ] 