from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *



@api_view(['POST'])
def register(request):
    user_serializer = UserSerializer(data=request.data)
    if user_serializer.is_valid():
        user_serializer.save()
        if not user_serializer.instance.is_patient:
            Doctor.objects.create(user=user_serializer.instance)
        return Response(user_serializer.data, status=201)
    return Response(user_serializer.errors, status=400)
