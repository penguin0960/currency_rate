import requests
from django.conf import settings

from monitoring.models import EuroCourse, EuroForecast


def send_message_in_telegram(message: str):
    if settings.TELEGRAM_CHANNEL_ID == '':
        print(f'Сообщение для телеги: "{message}"')

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


def notify_about_euro_forecast(forecast: EuroForecast):
    send_message_in_telegram(
        f'Прогноз евро на {forecast.date.strftime('%d.%m.%y')}: {forecast.forecast}.'
    )