from django.contrib import admin
from .models import (
    Slide, 
    CompanyAdvantage, 
    CompanyFact, 
    CompanyService, 
    CompanyInfo, 
    CooperationStage, 
    PopularQuestion, 
)


class CompanyFactInline(admin.TabularInline):
    model = CompanyFact
    extra = 1  
    verbose_name = "Факт"
    verbose_name_plural = "Факты о компании"


class CompanyServiceInline(admin.TabularInline):
    model = CompanyService
    extra = 1
    verbose_name = "Услуга"
    verbose_name_plural = "Услуги компании"


class CompanyAdvantageInline(admin.TabularInline):
    model = CompanyAdvantage
    extra = 1
    verbose_name = "Услуга"
    verbose_name_plural = "Услуги компании"


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin): 
    list_display = ['admin_panel_title']
    exclude = ['admin_panel_title']

    inlines = [
        CompanyFactInline, 
        CompanyServiceInline, 
        CompanyAdvantageInline
    ]  


@admin.register(CooperationStage)
class CooperationStageAdmin(admin.ModelAdmin): 
    list_display = ['name']
    search_fields = ['name']


@admin.register(PopularQuestion)
class PopularQuestionAdmin(admin.ModelAdmin): 
    list_display = ['question', 'answer']
    search_fields = ['question', 'answer']


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin): 
    list_display = ['title', 'price', 'photo']
    search_fields = ['title', 'description']