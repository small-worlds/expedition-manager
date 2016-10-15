from django.db import models


class Expedition(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, blank=False, default='')
    start_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(auto_now_add=False)
    min_jump = models.IntegerField()
    # has many Admins - see accounts?
    # belongs to one Admin - again, see accounts?
    # has many Members - again, see accounts?


class Waypoint(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    system = models.CharField(max_length=255, blank=False, default='')
    planet = models.CharField(max_length=5, blank=False, default='')
    expedition = models.ForeignKey(Expedition, on_delete=models.CASCADE)
    number = models.IntegerField()
