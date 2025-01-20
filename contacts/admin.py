from django.contrib import admin
from .models import (
    Worker,
    Request, 
    PrivacyPolicy, 
    PrivacyPolicyParagraph, 
    CertificatePhoto, 
    Partner,
)
from .filters import IsClosed


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin): 
    list_display = ['name', 'role', 'photo']


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin): 
    list_display = ['name', 'phone', 'created_at', 'is_closed']
    list_filter = [
        IsClosed
    ]


class PrivacyPolicyParagraphInline(admin.TabularInline):
    model = PrivacyPolicyParagraph
    extra = 1  
    verbose_name = "Абзац"
    verbose_name_plural = "Абзацы"


@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin): 
    list_display = ['__str__']
    inlines = [PrivacyPolicyParagraphInline]


@admin.register(CertificatePhoto)
class CertificatePhotoAdmin(admin.ModelAdmin): 
    list_display = ['__str__', 'photo']


@admin.register(Partner)
class PartnerImageAdmin(admin.ModelAdmin): 
    list_display = ['__str__', 'image']