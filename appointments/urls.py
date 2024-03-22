from django.urls import path
from .views import *

urlpatterns = [
    path('all_sch/', all_schedules, name='all_sch'),
    path('schedule/<int:s_id>/', schedule),
    path('all_app/', all_appointments, name='all_app'),
    path('appointment/<int:a_id>/', appointment),
    path('all_app/doctor/<int:doctor_id>/', doctor_appointments, name='doctor-appointments'),
    path('all_sch/doctor/<int:doctor_id>/', doctor_schedules, name='doctor-schedules'),
    path('all_app/user/<int:user_id>/', user_appointments, name='user-appointments'),
    path('pay/<int:appointment_id>/', handle_payment, name='handle-payment'),
]
