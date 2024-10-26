# myproject/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Установим переменную окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PClego.settings')

app = Celery('PClego')

# Загружаем настройки из конфигурационного файла Django с префиксом CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находим и регистрируем задачи в каждом приложении Django
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
