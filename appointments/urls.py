from django.urls import path
from .views import *

urlpatterns = [
    path('all_sch/', all_schedules, name='all_sch'),
    path('schedule/<int:s_id>/', schedule),
    path('all_app/', all_appointments, name='all_app'),
    path('appointment/<int:a_id>/', appointment),
     path('all_app/doctor/<int:doctor_id>/', doctor_appointments, name='doctor-appointments'),
]
