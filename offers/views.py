from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Offer
from .serializers import OfferSerializer
from doctors.models import Doctor

@api_view(['GET'])
def offer_list(request):
    if request.method == 'GET':
        offers = Offer.objects.all()
        if offers.exists():
            serializer = OfferSerializer(offers, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': 'There are no offers available'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def get_offers_by_doctor_id(request, doctor_id):
    # Check if the doctor exists
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    if request.method == 'GET':
        # Retrieve offers for the doctor
        offers = Offer.objects.filter(doctor=doctor)
        # Check if offers exist for the doctor
        if offers.exists():
            serializer = OfferSerializer(offers, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': 'No offers available for this doctor'}, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'POST':
        # Include doctor_id in the request data
        request.data['doctor'] = doctor_id
        # Create a new offer for the doctor
        serializer = OfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Fetch the created offer object
            created_offer = Offer.objects.get(pk=serializer.data['id'])
            # Update the serializer to include the doctor's name
            serializer_with_doctor_name = OfferSerializer(created_offer)
            return Response(serializer_with_doctor_name.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['PUT', 'DELETE'])
def update_delete_offer(request, doctor_id, offer_id):
    # Check if the doctor exists
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    # Check if the offer exists for the doctor
    offer = get_object_or_404(Offer, pk=offer_id, doctor=doctor)
    if request.method == 'PUT':
        # Include doctor_id in the request data
        request.data['doctor'] = doctor_id
        # Update the offer
        serializer = OfferSerializer(offer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        # Delete the offer
        offer.delete()
        return Response({'message': 'Offer deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

