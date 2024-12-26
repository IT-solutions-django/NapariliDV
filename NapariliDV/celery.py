import os 
from celery import Celery 
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NapariliDV.settings') 

app = Celery('NapariliDV') 
app.config_from_object('django.conf:settings', namespace='CELERY') 
app.autodiscover_tasks() 

app.conf.beat_schedule = {
    'update_reviews_from_2gis': {
        'task': 'reviews.tasks.update_2gis_reviews_task',
        'schedule': crontab(minute='*/30'), 
    },
    'update_reviews_from_vl': {
        'task': 'reviews.tasks.update_vl_reviews_task',
        'schedule': crontab(minute='*/30'), 
    },
    'update_reviews_from_yandex': {
        'task': 'reviews.tasks.update_yandex_reviews_task',
        'schedule': crontab(minute='*/30'), 
    },

    'refresh_amocrm_tokens': {
        'task': 'amocrm.tasks.refresh_tokens_task',
        'schedule': crontab(minute='*/30'),  
    },
}