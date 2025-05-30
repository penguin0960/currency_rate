from django.core.management import BaseCommand

from monitoring.models import EuroCourse
from monitoring.selectors import get_anex_euro_course_by_dates
from monitoring.telegram import notify_about_euro_course


class Command(BaseCommand):

    def handle(self, *args, **options):
        price_by_date = get_anex_euro_course_by_dates()
        for date, price in sorted(price_by_date.items(), key=lambda x: x[0]):
            euro_course, created = EuroCourse.objects.get_or_create(date=date, price=price)
            if created:
                notify_about_euro_course(euro_course)
