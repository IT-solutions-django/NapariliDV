from django import forms 
from .models import Request


class FeedbackForm(forms.ModelForm): 
    class Meta:
        model = Request
        fields = ['name', 'phone']
        labels = {
            'name': 'Имя',
            'phone': 'Телефон',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Ваше имя'
            }),
            'phone': forms.TextInput(attrs={
                'type': 'tel', 
                'placeholder': '+7'
            }),
        }