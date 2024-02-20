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

""" Start CRUD Work_with_operations """

class CreateWork_with_operations(ListCreateAPIView):
    queryset = models.Work_with_operations.objects.all()
    serializer_class = serializers.Work_with_operationSerializer


class UpdateWork_with_operations(UpdateAPIView):
    queryset = models.Work_with_operations.objects.all()
    serializer_class = serializers.Work_with_operationSerializer


class DeleteWork_with_operations(DestroyAPIView):
    queryset = models.Work_with_operations.objects.all()
    serializer_class = serializers.Work_with_operationSerializer

""" End CRUD Work_with_operations """


""" Start CRUD Clinical_statistics """

class CreateClinical_statistics(ListCreateAPIView):
    queryset = models.Clinical_statistics.objects.all()
    serializer_class = serializers.Clinical_statisticSerializer


class UpdateClinical_statistics(UpdateAPIView):
    queryset = models.Clinical_statistics.objects.all()
    serializer_class = serializers.Clinical_statisticSerializer


class DeleteClinical_statistics(DestroyAPIView):
    queryset = models.Clinical_statistics.objects.all()
    serializer_class = serializers.Clinical_statisticSerializer


""" End CRUD Work_with_operations """