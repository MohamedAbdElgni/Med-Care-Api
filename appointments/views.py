from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework import status
from django.shortcuts import get_object_or_404

from users.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .pagination import CustomPagination
# Create your views here.


@api_view(['GET', 'POST'])
def all_schedules(request):
    if request.method == 'GET':
        schedules = Schedule.objects.all()
        if schedules:
            serializer = ScheduleSerializer(schedules, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': 'No Schedules found'}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        print(request.data)
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def schedule(request, s_id):
    schedules = get_object_or_404(Schedule, pk=s_id)
    if request.method == 'GET':
        serializer = ScheduleSerializer(schedules)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ScheduleSerializer(schedules, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Schedule updated successfully', 'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        schedules.delete()
        return Response({'message': 'Schedule deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def all_appointments(request):
    if request.method == 'GET':
        
        appointments = Appointment.objects.all()
        
        if appointments:
            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': 'No Appointments found'}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #send_confirmation_email(request, serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def appointment(request, a_id):
    appointments = get_object_or_404(Appointment, pk=a_id)
    if request.method == 'GET':
        serializer = AppointmentSerializer(appointments)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AppointmentSerializer(appointments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            #send_confirmation_email(request, appointments)
            return Response({'message': 'Appointment updated successfully', 'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        appointments.delete()
        return Response({'message': 'Appointment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def doctor_appointments(request, doctor_id):
    """
    Get all appointment for a specific doctor
    with patient info in each appointment
    """
    queryset = Appointment.objects.filter(doctor=doctor_id).order_by('id')
    if not queryset:
        return Response({'message': 'No Appointment found for this doctor'}, status=status.HTTP_404_NOT_FOUND)
    else:
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = GetAppointmentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def user_appointments(request, user_id):
    """
    Get all appointment for a specific doctor
    with patient info in each appointment
    """
    queryset = Appointment.objects.filter(user=user_id).order_by('id')
    if not queryset:
        return Response({'message': 'No Appointment found for this doctor'}, status=status.HTTP_404_NOT_FOUND)
    else:
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = GetAppointmentForUserSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    
    

@api_view(['GET', 'POST'])
def doctor_schedules(request, doctor_id):
    """
    Get all schedules for a specific doctor
    or create a new schedule for the doctor
    """
    if request.method == 'GET':
        schedules = Schedule.objects.filter(doctor=doctor_id)
        if not schedules:
            return Response({'message': 'No schedules found for this doctor'}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = ScheduleSerializer(schedules, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        # Associate the doctor ID with the request data
        request.data['doctor'] = doctor_id
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# def send_confirmation_email(request, appointment):
#     """
#     Send confirmation email to the patient
#     """
#     print(appointment)
#     patient = User.objects.get(id=appointment['user'])
#     doctor = User.objects.get(id=appointment['doctor'])
#     schedule = Schedule.objects.get(id=appointment['schedule'])
#     subject = 'Appointment Confirmation'
#     message = render_to_string('appointment_confirmation_email.html', {
#         'patient': patient.username,
#         'doctor': doctor.username,
#         'appointment': schedule.day,
#         'start_time': schedule.start_time,
#         'end_time': schedule.end_time,
#         'is_accepted': 'Accepted' if appointment['is_accepted'] else 'Pending'
#     })
    
#     email = EmailMessage(
#         subject,
#         message,
#         to=[patient.email]
#     )
#     email.content_subtype = 'html'
#     email.send()
#     return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)