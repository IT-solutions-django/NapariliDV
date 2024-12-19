import os
from celery import shared_task 
from dotenv import load_dotenv
from .models import (
    Review, 
    Platform, 
    ReviewPhoto
)
from django.db import connection
from .services import (
    get_2gis_reviews_data, 
    get_vl_reviews_data,
)
from .exceptions import (
    EmptyReviewList, 
    UpdateReviewError
)


load_dotenv()


@shared_task(bind=True, max_retries=5)
def update_reviews_task(self) -> None: 
    # 2GIS
    TWO_GIS_API_KEY = os.getenv('2GIS_API_KEY')
    TWO_GIS_ID = os.getenv('2GIS_ORGANIZATION_ID')

    two_gis_platform, _ = Platform.objects.get_or_create('2GIS')
    vl_platform, _ = Platform.objects.get_or_create('VL')

    try:
        reviews_data = get_2gis_reviews_data(
            api_key_2gis=TWO_GIS_API_KEY, 
            organization_id=TWO_GIS_ID,
            reviews_limit=10
        )
        print(reviews_data) 

    except EmptyReviewList as e: 
        print('Список отзывов пуст') 
        return

    Review.objects.all().delete() 

    for review_data in reviews_data['reviews']: 
        new_review = Review(
            rate=review_data['stars'], 
            author=review_data['author'], 
            author_avatar=review_data['author_avatar'], 
            content=review_data['text'], 
            created_at=review_data['created_at'], 
            platform=two_gis_platform,
        )
        new_review.save()
        if review_data.get('photos'): 
            for photo_url in review_data['photos']: 
                new_photo = ReviewPhoto(
                    url=photo_url, 
                    review=new_review,
                )
                new_photo.save() 

    # VL Справочник
    try: 
        reviews_data = get_vl_reviews_data()
    except Exception as e:
        print(f'Произошла ошибка: {e}') 

    new_review = Review(
        rate=review_data['stars'], 
        author=review_data['author'], 
        author_avatar=review_data['author_avatar'], 
        content=review_data['text'], 
        created_at=..., 
        platform=vl_platform,
    )
    new_review.save()
    
