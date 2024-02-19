from django.shortcuts import render
from main import models
from main import serializers
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView

""" Start CRUD Employee """
class CreateEmployee(ListCreateAPIView):
     queryset = models.Employee.objects.all()
     serializer_class = serializers.EmployeeSerializer


class UpdateEmployee(UpdateAPIView):
    queryset = models.Employee
    serializer_class = serializers.EmployeeSerializer


class DeleteEmployee(DestroyAPIView):
    queryset = models.Employee
    serializer_class = serializers.EmployeeSerializer

""" End CRUD Employee """


