from celery import Celery
import os

celery = Celery(os.environ.get('FLASK_APP'), backend=os.environ.get('CELERY_BACKEND'),
                broker=os.environ.get('CELERY_BROKER_URL'))

# Celery Method
# def makeCelery(app):
#     celery = Celery(os.environ.get('FLASK_APP'), backend=os.environ.get('CELERY_BACKEND'),
#                     broker=os.environ.get('CELERY_BROKER_URL'))
#     celery.conf.update(app.config)
#     TaskBase = celery.Task
#
#     class ContextTask(TaskBase):
#         abstract = True
#
#         def __call__(self, *args, **kwargs):
#             with app.app_context():
#                 return TaskBase.__call__(self, *args, **kwargs)
#
#     celery.Task = ContextTask
#     return celery
