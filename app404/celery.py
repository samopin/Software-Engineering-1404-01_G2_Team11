import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app404.settings')

app = Celery('app404')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.include = [
    'team2.tasks.tasks',
    'team2.tasks.indexing',
]
