import requests
from django.conf import settings
from django.core.management import BaseCommand

from monitoring.selectors import get_anex_euro_course


class Command(BaseCommand):

    def handle(self, *args, **options):
        price_today = get_anex_euro_course()
        remains_rub = price_today * settings.REMAINS_EURO
        url = "https://api.telegram.org/bot"
        url += settings.BOT_TOKEN
        method = url + "/sendMessage"

        requests.post(method, data={
            "chat_id": settings.TELEGRAM_CHANNEL_ID,
            "text": f'Курс евро сейчас: {price_today} рублей. Осталось внести: {remains_rub} рублей'
        })
