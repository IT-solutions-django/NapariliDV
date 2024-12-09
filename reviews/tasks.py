import os
from celery import shared_task 
from dotenv import load_dotenv
from .models import Review 
from django.db import connection


load_dotenv()


@shared_task(bind=True, max_retries=5)
def update_reviews_task(self) -> None: 
    gis_api_key = os.getenv('2GIS_API_KEY')
    organization_id = os.getenv('2GIS_ORGANIZATION_ID')

    
