from django import forms 
from django.db import models
from .models import (
    Project, 
    Category, 
    Material, 
    RoofType, 
)
from .templatetags.price_filters import price_format
from .services import (
    get_max_project_price, 
    get_min_project_price, 
    get_max_project_square, 
    get_min_project_square
)


class CatalogFiltersForm(forms.Form): 
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)

        self.max_product_price = round(get_max_project_price(), 0)
        self.fields['price_max'].widget.attrs['max'] = self.max_product_price
        self.fields['price_max'].widget.attrs['placeholder'] = f'{price_format(self.max_product_price)} ₽'

        self.min_product_price = round(get_min_project_price(), 0)
        self.fields['price_min'].widget.attrs['min'] = self.min_product_price
        self.fields['price_max'].widget.attrs['max'] = self.max_product_price
        self.fields['price_min'].widget.attrs['placeholder'] = f'{price_format(self.min_product_price)} ₽'

        self.fields['price_min'].widget.attrs['min'] = self.min_product_price

        self.fields['categories'].choices = [(category.id, category.name) for category in Category.objects.all()]
        self.fields['materials'].choices = [(None, "Все")] + [(material.id, material.name) for material in Material.objects.all()]
        self.fields['roof_types'].choices = [(None, "Все")] + [(roof_type.id, roof_type.name) for roof_type in RoofType.objects.all()]


    categories = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )
    materials = forms.ChoiceField(
        widget=forms.Select(),
        required=False,
        label="Выберите материал",
        choices=[],
    )

    roof_types = forms.ChoiceField(
        widget=forms.Select(),
        required=False,
        label="Выберите тип кровли",
        choices=[],
    )
    price_min = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        label='Мин. цена',
        widget=forms.NumberInput(
            attrs={ 
                # 'step': 100000,
            }
        ), 
    )
    price_max = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        widget=forms.NumberInput(
            attrs={ 
                # 'step': 100000,
            }
        ), 
    )
    square_min = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        widget=forms.NumberInput(
            attrs={ 
                'placeholder': '80', 
                'min': 80,
                'max': 120,
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
                'placeholder': '120', 
                'min': 0,
                'max': 120,
                'step': 5,
            }
        ), 
    )
    floors_quantity = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 3)],  
        required=False,
        widget=forms.RadioSelect(attrs={
            'class': 'radio-toggle'
        }),
    )
    bedrooms_quantity = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 5)],
        required=False,
        widget=forms.RadioSelect(attrs={
            'class': 'radio-toggle'
        }),
    )
    bathrooms_quantity = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 4)], 
        required=False,
        widget=forms.RadioSelect(attrs={
            'class': 'radio-toggle'
        }),
    )