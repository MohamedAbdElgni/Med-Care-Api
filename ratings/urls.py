import os
from django.urls import path
from .views import *
urlpatterns = [
    #rating
    path('ratings/', all_ratings, name='all-ratings'), 
    path('ratings/<int:rating_id>/', rating_detail, name='rating-detail'), 
    #update
    path('ratings/doctor/<int:doctor_id>/', doctor_ratings, name='doctor-ratings'),


]
