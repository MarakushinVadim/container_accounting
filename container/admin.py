from django.contrib import admin

from container.models import Container


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    list_display = ('number', 'manufacture_year', 'status_hydrotesting', 'volume', 'client', 'on_refueling')
    search_fields = ('number', 'client', 'on_refueling')
