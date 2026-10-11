import io
from django.db.migrations import serializer
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render 
from .models import Person
from .serializers import  PersonModelSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
# Create your views here.


# @api_view(['GET', 'PUT', 'PATCH'])
# def singleobj(request, id):
#     data = get_object_or_404(Person, id=id)
#     if request.method == "PUT":
#         parsed_data = request.data
#         serializer = PersonModelSerializer(data, data=parsed_data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Updated'}, status=201)
#         return Response(serializer.errors, status=400)
    
#     if request.method == "PATCH":
#         parsed_data = request.data
#         serializer = PersonModelSerializer(data, data=parsed_data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Updated'}, status=201)
#         return Response(serializer.errors, status=400)
    
#     if request.method == "GET":
#         serializer = PersonModelSerializer(data)
#         return Response(serializer.data)

# @api_view(['GET', 'POST'])
# def multipleobj(request):
#     if request.method == 'POST':
#         parsed_data = request.data
#         serializer = PersonModelSerializer(data=parsed_data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Created'}, status=201)
#         return Response(serializer.errors, status=400)
    
#     if request.method == 'GET':
#         print(request.accepted_renderer)
#         data = Person.objects.all() 
#         serializer = PersonModelSerializer(data, many=True)
#         return Response(serializer.data)

    
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_yasg.utils import swagger_auto_schema

class singleobjAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer

class multipleobjAPIView(ListCreateAPIView):
    permission_classes = [AllowAny] # This makes the endpoint public
    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer

    @swagger_auto_schema(
        operation_description="Create a new person record",
        responses={201: PersonModelSerializer, 400: "Validation error"}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


# def get(self, request, *args, **kwargs):
#         print(request.user)
#         response = super().get(request, *args, **kwargs)
#         return response
