from pidgeotto.celery import app
from .models import Promotion


@app.task
def updateWeekAge():
    for promotion_age in Promotion.objects.all():
        promotion_age.age_days += 1
        promotion_age.save()

    for promotion in Promotion.objects.all():
        if promotion.age_days % 7 == 0:
            promotion.week_age += 1
            promotion.save()