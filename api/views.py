import io

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer, PersonModelSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET', 'PUT', 'PATCH'])
def singleobj(request, id):
    data = get_object_or_404(Person, id=id)
    if request.method == "PUT":
        parsed_data = request.data
        serializer = PersonModelSerializer(data, data=parsed_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'}, status=201)
        return Response(serializer.errors, status=400)
    
    if request.method == "PATCH":
        parsed_data = request.data
        serializer = PersonModelSerializer(data, data=parsed_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'}, status=201)
        return Response(serializer.errors, status=400)
    
    if request.method == "GET":
        serializer = PersonModelSerializer(data)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def multipleobj(request):
    if request.method == 'POST':
        parsed_data = request.data
        serializer = PersonModelSerializer(data=parsed_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=201)
        return Response(serializer.errors, status=400)
    
    if request.method == 'GET':
        print(request.accepted_renderer)
        data = Person.objects.all() 
        serializer = PersonModelSerializer(data, many=True)
        return Response(serializer.data)