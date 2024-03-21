from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from rest_framework import viewsets

class ContactMessage(viewsets.ModelViewSet):
    
    serializer_class = ContactMessageSerializer

    queryset = ContactMessage.objects.all()
# Create your views here.
