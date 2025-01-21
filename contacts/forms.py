from django import forms 
from .models import Request
from projects.models import Category


class FeedbackForm(forms.ModelForm): 
    class Meta:
        model = Request
        fields = ['name', 'phone', 'message']
        labels = {
            'name': 'Имя',
            'phone': 'Телефон',
            'message': 'Сообщение'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Ваше имя'
            }),
            'phone': forms.TextInput(attrs={
                'type': 'tel', 
                'placeholder': '+7'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Сообщение',
                'rows': 3
            })
        }


class GalleryFilterForm(forms.Form):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.fields['category'].choices = [(category.id, category.name) for category in Category.objects.all()]

    category = forms.ChoiceField(
            choices=[],  
            required=False,
            widget=forms.RadioSelect(attrs={
                'class': 'radio-toggle'
            }),
        )