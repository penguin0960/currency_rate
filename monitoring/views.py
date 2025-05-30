import datetime

from django.conf import settings
from django.shortcuts import render

from monitoring.selectors import get_anex_euro_course_by_dates


def check_euro_now(request):
    euro_by_date = get_anex_euro_course_by_dates()
    # euro_by_date = {datetime.date(2025, 5, 31): 95.05, datetime.date(2025, 5, 29): 96.21, datetime.date(2025, 5, 30): 94.73}
    euro_on_nearest_dates = [
        {
            'date': euro_in_day[0],
            'price': euro_in_day[1],
            'remains_rubs': round(euro_in_day[1] * settings.REMAINS_EURO),
        }
        for euro_in_day in euro_by_date.items()
    ]
    euro_on_nearest_dates.sort(key=lambda x: x['date'], reverse=True)
    return render(
        request,
        'monitoring/check_euro_today.html',
        context={
            'euro_on_nearest_dates': euro_on_nearest_dates,
            'remains_euro': settings.REMAINS_EURO,
        },
    )
