import requests
from django.conf import settings

from monitoring.models import EuroCourse


def send_message_in_telegram(message: str):
    requests.post(
        f'https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage',
        data={
            "chat_id": settings.TELEGRAM_CHANNEL_ID,
            "text": message,
        },
    )


def notify_about_euro_course(euro: EuroCourse):
    send_message_in_telegram(
        f'Курс евро на {euro.date.strftime('%d.%m.%y')} составляет {euro.price} руб. '
        f'По данному курсу остается внести {round(euro.remain_rubs)} руб.'
    )