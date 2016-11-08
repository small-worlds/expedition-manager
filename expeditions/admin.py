from django.contrib import admin
from expeditions.models import Expedition, Waypoint
# Register your models here.

class ExpeditionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_date', 'end_date', 'published')


class WaypointAdmin(admin.ModelAdmin):
    list_display = ('id', 'expedition', 'name', 'system', 'planet', 'datetime')
    list_filter = ('expedition', )

admin.site.register(Expedition, ExpeditionAdmin)
admin.site.register(Waypoint, WaypointAdmin)