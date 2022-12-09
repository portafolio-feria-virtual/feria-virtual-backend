import os
from celery import Celery
from datetime import timedelta
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_feria.settings')
app = Celery('back_feria')
app.config_from_object('django.conf:settings', namespace='CELERY')
 
app.conf.timezone = 'America/Santiago'
 
app.conf.beat_schedule = {
    "check_contract_date": {
        "task": "Apps.serviciosInternos.tasks.check_contract_date",
        "schedule": timedelta(seconds=10),
    },
}
 
app.autodiscover_tasks()
 
 