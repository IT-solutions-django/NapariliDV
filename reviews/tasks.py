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
    get_yandex_reviews_data
)
from .exceptions import (
    EmptyReviewList, 
    UpdateReviewError
)


load_dotenv()


@shared_task(bind=True, max_retries=5)
def update_vl_reviews_task(self) -> None:
    REVIEWS_COUNT_PER_PLATFORM = 10
    vl_platform, _ = Platform.objects.get_or_create(name='VL')
    try: 
        reviews_data, average_rating, reviews_count = get_vl_reviews_data()
    except Exception as e:
        print(f'Произошла ошибка при получении отзывов с VL.ru: {e}') 
        return
    Review.objects.filter(platform=vl_platform).delete()

    for review_data in reviews_data[:REVIEWS_COUNT_PER_PLATFORM]: 
        new_review = Review(
            rate=review_data['stars'], 
            author=review_data['author'], 
            author_avatar=review_data['author_avatar'], 
            content=review_data['text'], 
            created_at=review_data['created_at'], 
            platform=vl_platform,
        )
        new_review.save()

    vl_platform.average_rating = average_rating
    vl_platform.reviews_count = reviews_count
    vl_platform.save()


@shared_task(bind=True, max_retries=5)
def update_yandex_reviews_task(self) -> None:
    REVIEWS_COUNT_PER_PLATFORM = 10
    yandex_platform, _ = Platform.objects.get_or_create(name='Яндекс Карты')
    try: 
        reviews_data, average_rating, reviews_count = get_yandex_reviews_data()
    except Exception as e:
        print(f'Произошла ошибка при получении отзывов с Яндекс.Карт: {e}') 
        return
    Review.objects.filter(platform=yandex_platform).delete()

    for review_data in reviews_data[:REVIEWS_COUNT_PER_PLATFORM]: 
        new_review = Review(
            rate=review_data['stars'], 
            author=review_data['author'], 
            author_avatar=review_data['author_avatar'], 
            content=review_data['text'], 
            created_at=review_data['created_at'], 
            platform=yandex_platform,
        )
        new_review.save()
        if review_data.get('photos'): 
            for photo_url in review_data['photos'][:3]: 
                new_photo = ReviewPhoto(
                    url=photo_url, 
                    review=new_review,
                )
                new_photo.save()

        yandex_platform.average_rating = average_rating
        yandex_platform.reviews_count = reviews_count
        yandex_platform.save()



@shared_task(bind=True, max_retries=5)
def update_2gis_reviews_task(self) -> None:
    REVIEWS_COUNT_PER_PLATFORM = 10
    TWO_GIS_API_KEY = os.getenv('2GIS_API_KEY')
    TWO_GIS_ID = os.getenv('2GIS_ORGANIZATION_ID')
    two_gis_platform, _ = Platform.objects.get_or_create(name='2GIS')

    try:
        reviews_data, average_rating, reviews_count = get_2gis_reviews_data(
            api_key_2gis=TWO_GIS_API_KEY, 
            organization_id=TWO_GIS_ID,
            reviews_limit=REVIEWS_COUNT_PER_PLATFORM
        )
    except UpdateReviewError as e: 
        raise self.retry(exc=e, countdown=15)
    except EmptyReviewList as e: 
        raise self.retry(exc=e, countdown=15)
    Review.objects.filter(platform=two_gis_platform).delete()

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
            for photo_url in review_data['photos'][:3]: 
                new_photo = ReviewPhoto(
                    url=photo_url, 
                    review=new_review,
                )
                new_photo.save()

    two_gis_platform.average_rating = average_rating
    two_gis_platform.reviews_count = reviews_count
    two_gis_platform.save()