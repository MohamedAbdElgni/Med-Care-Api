from django.urls import path
from . import views

urlpatterns = [
    path('doctors/', views.offer_list, name='offer-list'),
    path('doctors/<int:doctor_id>/', views.get_offers_by_doctor_id, name='get-offers-by-doctor-id'),
    path('doctors/<int:doctor_id>/<int:offer_id>/', views.update_delete_offer, name='update-delete-offer'),


 

]

