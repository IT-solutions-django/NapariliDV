from django.contrib import admin
from .models import (
    Article, 
    Paragraph,
    ArticleType,
)


class ParagraphInline(admin.TabularInline):
    model = Paragraph
    extra = 1  
    verbose_name = "Абзац"
    verbose_name_plural = "Абзацы"


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin): 
    list_display = ['title', 'created_at']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ParagraphInline]