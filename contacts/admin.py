from django.contrib import admin
from .models import (
    Worker,
    Request, 
    GalleryPhoto,
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