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
    # Check if the user is a doctor
    if user.is_doctor:
        doctor_profile = Doctor.objects.get(user=user)
        doctor_serializer = DoctorSerializer(doctor_profile) 
        return Response({'token': token.key, 'user': serializer.data, 'doctor_profile': doctor_serializer.data})
    
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
    return Response({'message': f'Test view for {dir(request.user)}'})



@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout_user(request):
    request.auth.delete()
    return Response({'message': 'User logged out successfully'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_doctors(request):
    doctors = Doctor.objects.all()
    for doctor in doctors:
        print(doctor)
    serializer = DoctorSerializer(doctors, many=True)
    return Response(serializer.data)
