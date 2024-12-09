from .models import Project
from django.db import models
from decimal import Decimal


def get_max_project_price() -> Decimal: 
    max_price = Project.objects.aggregate(models.Max('price'))['price__max']
    return max_price

def get_min_project_price() -> Decimal: 
    min_price = Project.objects.aggregate(models.Min('price'))['price__min']
    return min_price

def get_max_project_square() -> float: 
    max_square = Project.objects.aggregate(models.Max('square'))['square__max']
    return max_square

def get_min_project_square() -> float: 
    min_square = Project.objects.aggregate(models.Min('square'))['square__min']
    return min_square