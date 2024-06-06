
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Установите переменную окружения для настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_platform.settings')

app = Celery('job_platform')

# Используйте конфигурации из settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение задач в приложениях Django
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


