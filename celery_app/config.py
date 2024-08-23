
from celery import Celery

from settings import settings

celery_app = Celery(
    "tasks",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_BACKEND_URL
)

celery_app.conf.update(
    result_expires=settings.CELERY_RESULT_LIFESPAN, 
)

# You can adjust the path or add a new path
celery_app.autodiscover_tasks(['celery_app.tasks'])