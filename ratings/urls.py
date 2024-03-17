import os
from django.urls import path
from .views import *
urlpatterns = [
    #rating
    path('', all_ratings, name='all-ratings'), 
    path('<int:rating_id>/', rating_detail, name='rating-detail'), 
    #update
    path('doctor/<int:doctor_id>/', doctor_ratings, name='doctor-ratings'),


]
