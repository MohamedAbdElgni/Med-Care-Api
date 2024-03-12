from django.db import models
from users.models import *


# Create your models here.
class Schedule(models.Model):
    weekday_choices = (
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
    )
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    day = models.CharField(max_length=9, choices=weekday_choices)
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)
    is_active = models.BooleanField(default=True)


class Appointment(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)
