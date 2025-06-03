from django.contrib import admin

from monitoring.models import EuroCourse, EuroForecast


@admin.register(EuroCourse)
class EuroCourseAdmin(admin.ModelAdmin):
    pass


@admin.register(EuroForecast)
class EuroForecastAdmin(admin.ModelAdmin):
    pass
