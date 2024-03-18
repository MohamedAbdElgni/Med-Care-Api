from pyexpat.errors import messages
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from .models import *
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect
from doctors.models import *
from.tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, f'Account activated successfully')
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link')
        
    return redirect('Home')
def activateEmail(request,user,email):
    mail_subject="Activate your user account"
    mail_msg = render_to_string('templeat_activate.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http',
    })
    email=EmailMessage(mail_subject,mail_msg,to=[email])
    if email.send(fail_silently=False):
        messages.success(request, f'Account created successfully. Please check {email} to activate your account')
    else:
        messages.error(request, f'Failed to send activation email to {email}')
    
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        print("-"*50)
        print((request.data))
        print("-"*50)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # User.is_active=False
            serializer.save()
            # activateEmail(request, user,form.cleaned_data.get['email'])
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
        user = get_object_or_404(User, email=request.data['email'])
        user.is_active=False
        if not user.check_password(request.data['password']):
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user)
        return Response({'token': token.key, 'user': serializer.data})
    

@api_view(['GET'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def test(request):
    """
    Test view
    to test authentication if user is logged in or not
    
    """
    print(request.user)
    print(request.auth)
    return Response({'message': f'Test view for {request.user.username}'})



@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout_user(request):
    request.auth.delete()
    return Response({'message': 'User logged out successfully'}, status=status.HTTP_200_OK)
    
        

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def get_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PATCH':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)

