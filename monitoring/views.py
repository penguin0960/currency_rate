import datetime

from django.conf import settings
from django.shortcuts import render

from monitoring.models import EuroCourse


def check_euro_now(request):
    today_course = EuroCourse.objects.filter(date=datetime.date.today()).order_by('dt_created').last()
    days_before_last_day_for_payment = (settings.LAST_DAY_FOR_PAYMENT - datetime.date.today()).days
    return render(
        request,
        'monitoring/check_euro_today.html',
        context={
            'euro_on_nearest_dates': EuroCourse.objects.order_by('-date')[:5],
            'today_euro_course': today_course,
            'remains_euro': settings.REMAINS_EURO,
            'deposited_euro': settings.DEPOSITED_EURO,
            'deposited_rubs': settings.DEPOSITED_RUBS,
            'need_pay_every_day': today_course and round(today_course.remain_rubs / days_before_last_day_for_payment),
            'money_progress_percent': round(settings.DEPOSITED_EURO * 100 / settings.FULL_PRICE_EURO),
            'days_before_departure': (settings.DEPARTURE_DATE - datetime.date.today()).days,
            'days_before_last_day_for_payment': (settings.LAST_DAY_FOR_PAYMENT - datetime.date.today()).days,
        },
    )
