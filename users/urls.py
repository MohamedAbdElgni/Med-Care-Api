import os
from django.urls import path
from .views import *



urlpatterns = [
    
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('patients/', get_patients, name='get_patients'),
    path('users/<int:user_id>/',user_details, name='user_details'),
    path('test/', test, name='test'),
]
