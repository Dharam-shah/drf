from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoApp
from .serializers import TodoAppSearilizers
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# def test(request):
#     return HttpResponse("test")

"""List and Create"""
# class TodoAppLC(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = TodoApp.objects.all()
#     serializer_class = TodoAppSearilizers  

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

"""Retrive, Update and Delete and Create"""
# class TodoAppRUD(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = TodoApp.objects.all()
#     serializer_class = TodoAppSearilizers

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

""""modelviewsets"""
class TodoAppCRUD(viewsets.ModelViewSet):
    queryset = TodoApp.objects.all()
    serializer_class = TodoAppSearilizers
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
