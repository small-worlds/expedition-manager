from django.db import models
from django.contrib.auth.models import User

def calculate_registration_number(expedition):
    present_keys = Registration.objects.filter(expedition=expedition).order_by('-registration_number').values_list('registration_number', flat=True)
    if present_keys:
        return present_keys[0] + 1
    else:
        return 1

class Expedition(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, blank=False, default='')
    start_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(auto_now_add=False)
    min_jump = models.IntegerField(blank=False)
    # how to handle roles? Do we WANT roles?
    # has many Admins - see accounts?
    # belongs to one Admin - again, see accounts?
    # has many Members - again, see accounts?


class Waypoint(models.Model):
    class Meta:
        unique_together = ('number', 'expedition')
        ordering = ['number']
    created = models.DateTimeField(auto_now_add=True)
    system = models.CharField(max_length=255, blank=False, default='')
    planet = models.CharField(max_length=5, blank=False, default='')
    expedition = models.ForeignKey(Expedition, on_delete=models.CASCADE, related_name='waypoints')
    number = models.IntegerField(blank=False)


class Registration(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registration')
    ship_model = models.CharField(max_length=50, blank=False)
    ship_name = models.CharField(max_length=255, blank=True, default='')
    ship_jump = models.DecimalField(max_digits=5, decimal_places=2)
    expedition = models.ForeignKey(Expedition, on_delete=models.CASCADE, related_name='registrations')
    registration_number = models.PositiveIntegerField()
    class Meta:
        unique_together = (('user', 'expedition'), ('registration_number', 'expedition'))

    def save(self, *args, **kwargs):
        registration_number = calculate_registration_number(self.expedition)
        self.registration_number = registration_number
        super(Registration, self).save(*args, **kwargs)