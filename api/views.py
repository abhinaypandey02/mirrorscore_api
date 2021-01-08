from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TaskSerializer

@api_view(['GET'])
def ping(request): #the ping request
    return Response({"status":"OK"})

@api_view(['POST'])
def schedule(request): #to schedule a get request
    serializer=TaskSerializer(data=request.data) #using taskserializer to add new entry to tasks
    if serializer.is_valid():
        serializer.save() #adding the new entry
    return Response(serializer.data)
