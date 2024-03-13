from django.urls import path
from .views import *

urlpatterns = [
    path('doctors/', get_doctors, name='get_doctors'),
    path('doctor/<int:doctor_id>/', doctor_details, name='doctor_details'),
]