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
        
# Patients --------------------------------------------------->    
@api_view(['GET'])
def get_patients(request):
    if request.method == 'GET':
        patients = User.objects.filter(is_patient=True, is_doctor=False)
        serializer = UserSerializer(patients, many=True)
        return Response(serializer.data)
    return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_details(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user.delete()
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

# Doctors --------------------------------------------------->    

@api_view(['GET'])
def get_doctors(request):
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)
    return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def doctor_details(request, doctor_id):
    try:
        doctor = Doctor.objects.get(user_id=doctor_id)
    except Doctor.DoesNotExist:
        return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        doctor.delete()
        return Response({'message': 'Doctor deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# Tokens --------------------------------------------------->    

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
    