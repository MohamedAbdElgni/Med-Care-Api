import os
from django.urls import path
from .views import *



urlpatterns = [
    
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('user/', user, name='user'),
    path('test/', test, name='test'),
    #rating
    path('ratings/', all_ratings, name='all-ratings'),  # New endpoint for all ratings
    path('rate/', rate_doctor, name='rate-doctor'),
    path('ratings/<int:doctor_id>/', doctor_ratings, name='doctor-ratings'),
]
