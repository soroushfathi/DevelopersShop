import os
from celery import Celery

PROJ_NAME = 'DevelopersShop'

os.environ.setdefault('DJANGO_SETTING_MODULE', f'{PROJ_NAME}.settings')

app = Celery(PROJ_NAME)

app.config_from_object('django.conf:setting', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
