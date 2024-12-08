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
        self.fields['price_max'].widget.attrs['placeholder'] = f'{self.max_product_price} ₽'

        self.fields['categories'].choices = [(category.id, category.name) for category in Category.objects.all()]

    categories = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class': ''
            }
        ),
        required=False
    )
    materials = forms.ChoiceField(
        widget=forms.Select(),
        required=False,
        label="Выберите материал",
        choices=[(material.id, material.name) for material in Material.objects.all()],
    )

    roof_types = forms.ChoiceField(
        widget=forms.Select(),
        required=False,
        label="Выберите тип кровли",
        choices=[(roof_type.id, roof_type.name) for roof_type in RoofType.objects.all()],
    )
    price_min = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        label='Мин. цена',
        widget=forms.NumberInput(
            attrs={ 
                'placeholder': '1 500 000', 
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
                'placeholder': '15 000 000', 
                'min': 0,
                'step': 100000,
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
                'step': 5,
            }
        ), 
    )
    floors_quantity = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 3)],  
        required=False,
        widget=forms.RadioSelect(),
    )
    bedrooms_quantity = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 5)],
        required=False,
        widget=forms.RadioSelect(attrs={
            'class': ''
        }),
    )
    bathrooms_quantity = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 4)], 
        required=False,
        widget=forms.RadioSelect(attrs={
            'class': ''
        }),
    )