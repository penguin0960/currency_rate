from django.conf import settings
from django.db import models


class EuroCourse(models.Model):

    dt_created = models.DateTimeField('Дата создания', auto_now_add=True)
    dt_updated = models.DateTimeField('Дата обновления', auto_now=True)

    price = models.FloatField('Цена в рублях')
    date = models.DateField('Дата, на которую актуален курс')

    class Meta:
        verbose_name = 'Курс евро'
        verbose_name_plural = 'Курсы евро'

    def __str__(self):
        return f'{self.date} - {self.price} руб.'

    @property
    def remain_rubs(self) -> float:
        return self.price * settings.REMAINS_EURO


class EuroForecast(models.Model):

    dt_created = models.DateTimeField('Дата создания', auto_now_add=True)
    dt_updated = models.DateTimeField('Дата обновления', auto_now=True)

    date = models.DateField('Дата, на которую актуален прогноз')
    forecast = models.CharField('Прогноз', max_length=255)

    class Meta:
        verbose_name = 'Прогноз евро'
        verbose_name_plural = 'Прогнозы евро'

    def __str__(self):
        return f'{self.date} - {self.forecast} руб.'
