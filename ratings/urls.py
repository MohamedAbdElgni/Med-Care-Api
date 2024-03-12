import os
from django.urls import path
from .views import *
urlpatterns = [
    #rating
    path('ratings/', all_ratings, name='all-ratings'), 
    path('ratings/<int:rating_id>/', rating_detail, name='rating-detail'), 



]
