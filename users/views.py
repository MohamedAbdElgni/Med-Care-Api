from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from .models import *
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404



@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            if request.data['is_doctor']:
                doctor = Doctor(user=User.objects.filter(username=request.data['username']).first())
                doctor.save()
                token = Token.objects.create(user=doctor.user)
                return Response({'token': token.key,'user': serializer.data})
            else:
                token = Token.objects.create(user=User.objects.filter(username=request.data['username']).first())
                return Response({'token': token.key,'user': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['POST'])
def login_user(request):
        user = get_object_or_404(User, username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user)
        return Response({'token': token.key, 'user': serializer.data})
        
    
@api_view(['GET'])
def user(request):
    pass


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test(request):
    """
    Test view
    to test authentication if user is logged in or not
    
    """
    return Response({'message': f'Test view for {request.user.email}'})



@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout_user(request):
    request.auth.delete()
    return Response({'message': 'User logged out successfully'}, status=status.HTTP_200_OK)
    
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
def doctor_ratings(request, doctor_id):
    try:
        user = User.objects.get(id=doctor_id, is_doctor=True)
        doctor = Doctor.objects.get(user=user)
    except User.DoesNotExist:
        return Response({'message': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
    except Doctor.DoesNotExist:
        return Response({'message': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        ratings = Rating.objects.filter(doctor=doctor)
        if not ratings:
            return Response({'message': 'No ratings found for this doctor'}, status=status.HTTP_404_NOT_FOUND)
        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        rating_id = doctor_id
        rating = get_object_or_404(Rating, id=rating_id)
        serializer = RatingSerializer(rating, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'message': 'Rating updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        rating_id = doctor_id
        rating = get_object_or_404(Rating, id=rating_id)
        rating.delete()
        return Response({'message': 'Rating deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

