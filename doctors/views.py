from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from .models import *
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from .pagination import CustomPagination


@api_view(['GET'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
def get_doctors(request):
    if request.method == 'GET':
        search_query = request.query_params.get('q', '')
        queryset = Doctor.objects.all().order_by('user__id')

        if search_query:
            queryset = queryset.filter(user__first_name__icontains=search_query)

        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = DoctorSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
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

