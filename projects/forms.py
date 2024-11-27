from django import forms 
from .models import (
    Project, 
    Category, 
    Material, 
    RoofType, 
)
from .services import get_max_project_price


class CatalogFiltersForm(forms.Form): 
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)

        self.max_product_price = round(get_max_project_price(), 0)
        self.fields['price_max'].widget.attrs['placeholder'] = f'До {self.max_product_price} ₽'

        self.fields['categories'].choices = [(category.id, category.name) for category in Category.objects.all()]
        self.fields['materials'].choices = [(material.id, material.name) for material in Material.objects.all()]
        self.fields['roof_types'].choices = [(roof_type.id, roof_type.name) for roof_type in RoofType.objects.all()]

    categories = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class': 'filters__checkbox'
            }
        ),
        required=False
    )
    materials = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class': 'filters__checkbox'
            }
        ),
        required=False
    )
    roof_types = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class': 'filters__checkbox'
            }
        ),
        required=False
    )
    price_min = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        label='Мин. цена',
        widget=forms.NumberInput(
            attrs={ 
                'class': 'filters__number-input', 
                'placeholder': 'От 0 ₽', 
                'min': 0,
                'step': 100000,
            }
        ), 
    )
    price_max = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        widget=forms.NumberInput(
            attrs={ 
                'class': 'filters__number-input', 
                'min': 0,
                'step': 100000,
            }
        ), 
    )
    square_min = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        label='Мин. цена',
        widget=forms.NumberInput(
            attrs={ 
                'class': 'filters__number-input', 
                'placeholder': 'От ...', 
                'min': 0,
                'step': 5,
            }
        ), 
    )
    square_max = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        widget=forms.NumberInput(
            attrs={ 
                'class': 'filters__number-input', 
                'placeholder': 'До ...', 
                'min': 0,
                'step': 5,
            }
        ), 
    )
