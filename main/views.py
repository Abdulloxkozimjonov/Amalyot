from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers

@api_view(["GET"])
def employ_by_age(request):
    age = request.GET.get("age")
    employee = models.Employee.objects.filter(age__icontains = age)
    ser = serializers.EmployeeSerializer(employee)
    return Response(ser.data)





