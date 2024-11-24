from .models import Project
from django.db import models
from decimal import Decimal


def get_max_project_price() -> Decimal: 
    max_price = Project.objects.aggregate(models.Max('price'))['price__max']
    return max_price