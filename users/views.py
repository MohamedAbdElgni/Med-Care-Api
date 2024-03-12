from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .models import *
from .serializers import *
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,get_user_model, login, logout
from rest_framework import status
import jwt, datetime
from rest_framework.decorators import authentication_classes, permission_classes
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from .tokens import *





@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            if request.data['is_doctor']:
                doctor = Doctor(user=User.objects.filter(username=request.data['username']).first())
                doctor.save()
                
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        user = User.objects.filter(username=username).first()
        if user is None:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        if not user.check_password(password):
            return Response({'error': 'Wrong password'}, status=status.HTTP_400_BAD_REQUEST)
        token = encode_token(user)
        response = Response()
        set_token_cookie(response, token)
        response.data = {
            'message': 'success'
        }
        return response
    return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)


    
@api_view(['GET'])
def user(request):
    token = request.COOKIES.get('jwt')
    if not token:
        return Response({'error': 'Not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        payload = decode_token(token)
    except jwt.ExpiredSignatureError:
        return Response({'error': 'Token expired'}, status=status.HTTP_401_UNAUTHORIZED)
    user = User.objects.filter(id=payload['id']).first()
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
def logout_user(request):
    response = Response()
    delete_token_cookie(response)
    response.data = {
        'message': 'success'
    }
    return response

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
#@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def test(request):
    """
    Test view
    to test authentication if user is logged in or not
    
    """
    return Response({'message': 'Test view'})




