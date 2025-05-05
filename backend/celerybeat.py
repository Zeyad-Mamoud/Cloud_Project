from celery import Celery
from celery.schedules import crontab

app = Celery('tasks', broker='redis://redis:6379/0')

app.conf.beat_schedule = {
    'check-reminders-every-day': {
        'task': 'tasks.check_reminders',
        'schedule': crontab(hour=0, minute=0),  # Runs every day at midnight
    },
}