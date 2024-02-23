from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers

api_view(['GET'])
def employee_by_name(request):
    name = request.GET.get('name')
    employee = models.Employee.objects.filter(name__icontains = name)
    ser = serializers.EmployeeSerializer(employee, many=True)
    return Response(ser.data)


api_view(['GET'])
def employee_by_age(request):
    age = request.GET.get('age')
    employee = models.Employee.objects.filter(age__icontains = age)
    ser = serializers.EmployeeSerializer(employee, many=True)
    return Response(ser.data)

api_view(['GET'])
def employee_by_experience (request):
    experience  = request.GET.get('experience')
    employee = models.Employee.objects.filter(experience__icontains = experience)
    ser = serializers.EmployeeSerializer(employee, many=True)
    return Response(ser.data)


