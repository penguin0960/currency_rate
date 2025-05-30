from django.conf import settings
from django.shortcuts import render

from monitoring.models import EuroCourse
from monitoring.selectors import get_anex_euro_course_by_dates
from monitoring.telegram import notify_about_euro_course


def check_euro_now(request):
    price_by_date = get_anex_euro_course_by_dates()
    euro_on_nearest_dates = []
    for date, price in sorted(price_by_date.items(), key=lambda x: x[0], reverse=True):
        euro_course, created = EuroCourse.objects.get_or_create(date=date, price=price)
        euro_on_nearest_dates.append(euro_course)
        if created:
            notify_about_euro_course(euro_course)

    return render(
        request,
        'monitoring/check_euro_today.html',
        context={
            'euro_on_nearest_dates': euro_on_nearest_dates,
            'remains_euro': settings.REMAINS_EURO,
        },
    )
