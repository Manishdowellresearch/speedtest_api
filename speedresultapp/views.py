from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q
from .models import Speed_test_data
from .serializers import SpeedSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def get_speed(request):
    serializer = SpeedSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)