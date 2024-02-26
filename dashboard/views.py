from django.shortcuts import render
from main import models
from main import serializers
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

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


class Employee_all(ListAPIView):
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

class Room_all(ListAPIView):
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


class Department_all(ListAPIView):
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


class Equpment_all(ListAPIView):
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


class Work_with_operations_all(ListAPIView):
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


class Clinical_statistics_all(ListAPIView):
    queryset = models.Clinical_statistics.objects.all()
    serializer_class = serializers.Clinical_statisticSerializer

""" End CRUD Clinical_statistics """

""" Start CRUD Payment """

class CreatePayment(ListCreateAPIView):
    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer


class UpdatePayment(UpdateAPIView):
    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer


class DeletePayment(DestroyAPIView):
    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer


class Paymnent_all(ListAPIView):
    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer

""" End CRUD Payment """

class CreateIncome(ListCreateAPIView):
    queryset = models.Income.objects.all()
    serializer_class = serializers.IncomeSerializer


class UpdateIncome(UpdateAPIView):
    queryset = models.Income.objects.all()
    serializer_class = serializers.IncomeSerializer



class DeleteIncome(DestroyAPIView):
    queryset = models.Income.objects.all()
    serializer_class = serializers.IncomeSerializer


class Income_all(ListAPIView):
    queryset = models.Income.objects.all()
    serializer_class = serializers.IncomeSerializer

""" End CRUD Income """

""" Create CRUD Attendance """

class CreateAttendance(ListCreateAPIView):
    queryset = models.Attendance.objects.all()
    serializer_class = serializers.AttendanceSerializer


class Attendance_all(ListAPIView):
    queryset = models.Attendance.objects.all()
    serializer_class = serializers.AttendanceSerializer

""" End CRUD Attendance """


""" Start CRUD Patients """
class CreatePatients(ListCreateAPIView):
    queryset = models.Patients.objects.all()
    serializer_class = serializers.PatientsSerializer


class UpdatePatients(UpdateAPIView):
    queryset = models.Patients.objects.all()
    serializer_class = serializers.PatientsSerializer



class DeletePatients(DestroyAPIView):
    queryset = models.Patients.objects.all()
    serializer_class = serializers.PatientsSerializer


class Patients_all(ListAPIView):
    queryset = models.Patients.objects.all()
    serializer_class = serializers.PatientsSerializer

""" End CRUD Patients """


""" Start CRUD Patient_info """
class CreatePatient_info(ListCreateAPIView):
    queryset = models.Patient_info.objects.all()
    serializer_class = serializers.Patient_infoSerializer


class UpdatePatient_info(UpdateAPIView):
    queryset = models.Patient_info.objects.all()
    serializer_class = serializers.Patient_infoSerializer



class DeletePatient_info(DestroyAPIView):
    queryset = models.Patient_info.objects.all()
    serializer_class = serializers.Patient_infoSerializer


class Pattient_info_all(ListAPIView):
    queryset = models.Patient_info.objects.all()
    serializer_class = serializers.Patient_infoSerializer

""" End CRUD Patient_info """


""" Start CRUD Injury """
class CreateInjury(ListCreateAPIView):
    queryset = models.Injury.objects.all()
    serializer_class = serializers.InjurySerializer


class UpdateInjury(UpdateAPIView):
    queryset = models.Patient_info.objects.all()
    serializer_class = serializers.InjurySerializer



class DeleteInjury(DestroyAPIView):
    queryset = models.Injury.objects.all()
    serializer_class = serializers.InjurySerializer


class Injury_all(ListAPIView):
    queryset = models.Injury.objects.all()
    serializer_class = serializers.InjurySerializer

""" End CRUD Injury """


""" Start CRUD Devices """
class CreateDevices(ListCreateAPIView):
    queryset = models.Devices.objects.all()
    serializer_class = serializers.DeviceSerializer


class UpdateDevices(UpdateAPIView):
    queryset = models.Devices.objects.all()
    serializer_class = serializers.DeviceSerializer



class DeleteDevices(DestroyAPIView):
    queryset = models.Devices.objects.all()
    serializer_class = serializers.DeviceSerializer


class Devices_all(ListAPIView):
    queryset = models.Devices.objects.all()
    serializer_class = serializers.DeviceSerializer

""" End CRUD Devices """





