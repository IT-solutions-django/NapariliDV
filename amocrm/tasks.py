from celery import shared_task 
from amocrm.services import crm
from loguru import logger


@shared_task
def refresh_tokens_task() -> None:
    crm.refresh_tokens()