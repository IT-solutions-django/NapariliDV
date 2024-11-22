from django.contrib import admin
from .models import (
    Slide, 
    CompanyAdvantage, 
    CompanyFact, 
    CompanyService, 
    CompanyInfo, 
    CooperationStage, 
    PopularQuestion
)


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin): 
    list_display = ['title', 'description', 'button_text']
    search_fields = ['title', 'description', 'button_text']


@admin.register(CompanyAdvantage)
class CompanyAdvantageAdmin(admin.ModelAdmin): 
    list_display = ['name', 'description']
    search_fields = ['name', 'description']


@admin.register(CompanyFact)
class CompanyFactAdmin(admin.ModelAdmin): 
    list_display = ['name']
    search_fields = ['name']


@admin.register(CompanyService)
class CompanyServiceAdmin(admin.ModelAdmin): 
    list_display = ['name']
    search_fields = ['name']


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin): 
    list_display = ['admin_panel_title']
    exclude = ['admin_panel_title']


@admin.register(CooperationStage)
class CooperationStageAdmin(admin.ModelAdmin): 
    list_display = ['name']
    search_fields = ['name']


@admin.register(PopularQuestion)
class PopularQuestionAdmin(admin.ModelAdmin): 
    list_display = ['question', 'answer']
    search_fields = ['question', 'answer']