from django.contrib import admin
from .models import (
    TwoGISReview,
)


@admin.register(TwoGISReview)
class TwoGISReviewAdmin(admin.ModelAdmin): 
    list_display = ['id', 'username', 'content', 'created_at']