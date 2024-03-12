from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from django.shortcuts import get_object_or_404

#rating  
@api_view(['GET', 'POST'])
def all_ratings(request):
    if request.method == 'GET':
        ratings = Rating.objects.all()
        if not ratings:  # Check if the queryset is empty
            return Response({'message': 'No ratings found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = RatingSerializer(ratings, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Assuming RatingSerializer handles all necessary fields
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def rating_detail(request, rating_id):
    rating = get_object_or_404(Rating, pk=rating_id)
    
    if request.method == 'GET':
        serializer = RatingSerializer(rating)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = RatingSerializer(rating, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Rating updated successfully', 'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        rating.delete()
        return Response({'message': 'Rating deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        #update
@api_view(['GET', 'PUT', 'DELETE'])
def doctor_ratings(request, doctor_id):
    try:
        # Retrieve the user with the specified ID
        user = User.objects.get(id=doctor_id)
        # Check if the user is a doctor
        if not user.is_doctor:
            return Response({'message': 'The specified user is not a doctor'}, status=status.HTTP_404_NOT_FOUND)
        # Retrieve all ratings for the specified doctor
        ratings = Rating.objects.filter(doctor_id=doctor_id) 
        if not ratings.exists():
            return Response({'message': 'No ratings found for this doctor'}, status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serializer = RatingSerializer(ratings, many=True)
            return Response(serializer.data)        
        elif request.method == 'DELETE':

            ratings.delete()
            return Response({'message': 'Doctor ratings deleted successfully'}, status=status.HTTP_204_NO_CONTENT) 
    except User.DoesNotExist:
        return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

