from django.contrib import admin
from .models import (
    Project, 
    Category, 
    Material, 
    RoofType, 
    Floor, 
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


class FloorInline(admin.TabularInline):
    model = Floor
    extra = 1
    verbose_name = 'Этаж'
    verbose_name_plural = 'Этажи'


class ProjectPhotoInline(admin.TabularInline): 
    model = ProjectPhoto
    extra = 0


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin): 
    list_display = ['id', 'name', 'description', 'square', 'price', 'rooms_quantity']

    inlines = [
        FloorInline,
        ProjectPhotoInline,
    ] 