from django.shortcuts import render






# simple end point to return a string for rest api framework

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

@api_view(['GET'])
def test_connection(request):
    return Response("congratulations, server is working!", status=200)

