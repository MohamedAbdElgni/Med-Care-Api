from django.urls import path
from .views import *

urlpatterns = [
    path('user/<int:user_id>/', get_questions, name='user-question-list'),

       

]

