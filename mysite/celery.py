import os
from celery import Celery
from celery.schedules import crontab
import blog

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'blog.tasks.send_mail_task',
        'schedule': crontab(),
        'args': ()
    },
}


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, blog.tasks.create_random_user_accounts.s(14), name='add every 10')

app.conf.timezone = 'Asia/Bishkek'
