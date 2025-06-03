import datetime

from django.core.management import BaseCommand

from monitoring.models import EuroCourse, EuroForecast
from monitoring.selectors import TourKassaParser
from monitoring.telegram import notify_about_euro_course, notify_about_euro_forecast


class Command(BaseCommand):

    def handle(self, *args, **options):
        parser = TourKassaParser()
        parser.parse()
        price_by_date = parser.get_anex_euro_course_by_dates()
        for date, price in sorted(price_by_date.items(), key=lambda x: x[0]):
            euro_course, created = EuroCourse.objects.get_or_create(date=date, price=price)
            if created:
                notify_about_euro_course(euro_course)

        date, forecast = parser.get_euro_forecast_with_date()
        actual_forecast = EuroForecast.objects.filter(date=datetime.date.today()).order_by('-dt_created').first()
        if not actual_forecast or actual_forecast.forecast != forecast:
            notify_about_euro_forecast(EuroForecast.objects.create(date=datetime.date.today(), forecast=forecast))
