from django.shortcuts import render
from main import models
from main import serializers
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView

""" Start CRUD Employee """
class CreateEmployee(ListCreateAPIView):
     queryset = models.Employee.objects.all()
     serializer_class = serializers.EmployeeSerializer


class UpdateEmployee(UpdateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer


class DeleteEmployee(DestroyAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer

""" End CRUD Employee """

""" Start CRUD Room """

class CreateRoom(ListCreateAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer


class UpdateRoom(UpdateAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer


class DeleteRoom(DestroyAPIView):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer

""" End CRUD Room """


""" Start CRUD Department """

class CreateDepartment(ListCreateAPIView):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer


class UpdateDepartment(UpdateAPIView):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer


class DeleteDepartment(DestroyAPIView):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer

""" End CRUD Department """


""" Start CRUD Equpment  """

class CreateEqupment(ListCreateAPIView):
    queryset = models.Equipment.objects.all()
    serializer_class = serializers.EquipmentSerializer


class UpdateEqupment(UpdateAPIView):
    queryset = models.Equipment.objects.all()
    serializer_class = serializers.EquipmentSerializer


class DeleteEqupment(DestroyAPIView):
    queryset = models.Equipment.objects.all()
    serializer_class = serializers.EquipmentSerializer

""" End CRUD Equpment """