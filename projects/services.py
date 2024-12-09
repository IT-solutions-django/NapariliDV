from django.db import models
from decimal import Decimal
from django.db.models.query import QuerySet
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Project


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

def get_paginated_collection(request, collection: QuerySet, count_per_page: int = 10): 
    paginator = Paginator(collection, count_per_page)
    page_number = request.GET.get('page', 1)
    try:
        collection = paginator.page(page_number)
    except PageNotAnInteger:
        collection = paginator.page(1)
    except EmptyPage:
        collection = paginator.page(paginator.num_pages) 
    return collection