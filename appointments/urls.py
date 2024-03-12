from django.urls import path
from .views import *

urlpatterns = [
    path('listSchedules/', all_schedules, name='all-schedules'),
    path('schedule/<int:s_id>', schedule),
    path('listAppointments/', all_appointments, name='all-appointments'),
    path('appointment/<int:a_id>', appointment),
]
