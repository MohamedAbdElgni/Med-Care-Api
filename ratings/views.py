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
