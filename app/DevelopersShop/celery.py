import os
from celery import Celery

PROJ_NAME = 'DevelopersShop'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{PROJ_NAME}.settings')

app = Celery(PROJ_NAME)

app.config_from_object('django.conf:settings', namespace='CELERY')

# app.autodiscover_tasks()
