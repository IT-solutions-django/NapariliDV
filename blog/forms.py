from django import forms 
from django.db import models
from .models import (
    Article, 
    ArticleType, 
    Paragraph,
)


class ArticlesForm(forms.Form): 
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)

        self.fields['article_type'].choices = [(article_type.id, article_type.name) for article_type in ArticleType.objects.all()]


    article_type = forms.ChoiceField(
        choices=[],  
        required=False,
        widget=forms.RadioSelect(attrs={
            'class': 'radio-toggle'
        }),
    )
