from django.contrib import admin

from monitoring.models import EuroCourse


@admin.register(EuroCourse)
class EuroCourseAdmin(admin.ModelAdmin):
    pass
