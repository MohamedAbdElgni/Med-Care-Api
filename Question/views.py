from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from users.models import User



@api_view(['GET', 'POST'])
def get_questions(request, user_id):
    # Check if the user exists
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'GET':
        # Retrieve questions for the user
        questions = Question.objects.filter(user=user)
        # Check if questions exist for the user
        if questions.exists():
            serializer = QuestionSerializer(questions, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': 'No questions available for this user'}, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'POST':
        # Include user_id in the request data
        request.data['user'] = user_id
        # Create a new question for the user
        serializer =UserQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


