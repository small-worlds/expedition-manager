from django.contrib import admin
from expeditions.models import Expedition, Waypoint
# Register your models here.

class ExpeditionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_date', 'end_date', 'published')
    search_fields = ('name', 'start_date')
    list_filter = ('published', )


class WaypointAdmin(admin.ModelAdmin):
    list_display = ('id', 'expedition', 'name', 'system', 'planet', 'datetime')
    list_filter = ('expedition', )
    search_fields = ('name', 'expedition__name', 'system', 'planet', 'datetime')

admin.site.register(Expedition, ExpeditionAdmin)
admin.site.register(Waypoint, WaypointAdmin)