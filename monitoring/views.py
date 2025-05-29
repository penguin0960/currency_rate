import requests
from bs4 import BeautifulSoup
from django.conf import settings
from django.shortcuts import render

from monitoring.selectors import get_anex_euro_course


def check_euro_today(request):
    price_today = get_anex_euro_course()
    return render(
        request,
        'monitoring/check_euro_today.html',
        context={
            'price_today': price_today,
            'remains_rub': price_today * settings.REMAINS_RUB,
        },
    )
