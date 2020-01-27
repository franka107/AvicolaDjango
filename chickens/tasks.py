from pidgeotto.celery import app
from .models import Promotion


@app.task
def updateWeekAge():
    for promotion in Promotion.objects.all():
        promotion.week_age += 1
        promotion.save()
    