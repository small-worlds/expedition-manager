from django.contrib import admin
from expeditions.models import Expedition, Waypoint, Registration
# Register your models here.

class ExpeditionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_date', 'end_date', 'published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'start_date')
    list_filter = ('published', )


class WaypointAdmin(admin.ModelAdmin):
    list_display = ('id', 'expedition', 'name', 'system', 'planet', 'datetime')
    list_display_links = ('id', 'name')
    list_filter = ('expedition', )
    search_fields = ('name', 'expedition__name', 'system', 'planet', 'datetime')


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'expedition', 'registration_number')
    list_display_links = ('id', 'user')
    list_filter = ('expedition', 'user')
    search_fields = ('user__username', 'expedition__name')


admin.site.register(Expedition, ExpeditionAdmin)
admin.site.register(Waypoint, WaypointAdmin)
admin.site.register(Registration, RegistrationAdmin)