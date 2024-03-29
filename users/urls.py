import os
from django.urls import path
from .views import *



urlpatterns = [
    
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('users/<int:id>/', get_user, name='get_user'),
    path('test/', test, name='test'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('users/change-password/<int:id>/', ChangePasswordView.as_view(), name='change_password'),

]
