from django.contrib import admin
from .models import (
    Slide, 
    CompanyInfo, 
    CooperationStage, 
    PopularQuestion, 
)


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


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin): 
    list_display = ['title', 'price', 'photo']
    search_fields = ['title', 'description']