from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers

@api_view(["GET"])
def employ_by_age(request):
    age = request.GET.get("age")
    employee = models.Employee.objects.filter(age__icontains=age)
    ser = serializers.EmployeeSerializer(employee)
    return Response(ser.data)

@api_view(["GET"])
def employ_by_full_name(request):
    full_name = request.GET.get("full_name")
    employee = models.Employee.objects.filter(full_name__icontains=full_name)
    ser = serializers.EmployeeSerializer(employee)
    return Response(ser.data)


@api_view(["GET"])
def employ_by_status(request):
    status = request.GET.get("status")
    employee = models.Employee.objects.filter(status=status)
    ser = serializers.EmployeeSerializer(employee)
    return Response(ser.data)


@api_view(["GET"])
def employ_by_work_time(request):
    work_time = request.GET.get("work_time")
    employee = models.Employee.objects.filter(work_time=work_time)
    ser = serializers.EmployeeSerializer(employee)
    return Response(ser.data)


@api_view(["GET"])
def employ_by_experience(request):
    experience = request.GET.get("experience")
    employee = models.Employee.objects.filter(experience__icontains=experience)
    ser = serializers.EmployeeSerializer(employee)
    return Response(ser.data)


@api_view(["GET"])
def employ_by_department(request):
    department = request.GET.get("department")
    employee = models.Employee.objects.filter(department=department)
    ser = serializers.EmployeeSerializer(employee)
    return Response(ser.data)


@api_view(["GET"])
def employ_by_salary(request):
    salary = request.GET.get("salary")
    employee = models.Employee.objects.filter(salary=salary)
    ser = serializers.EmployeeSerializer(employee)
    return Response(ser.data)



@api_view(["GET"])
def employ_by_room(request):
    room = request.GET.get("room")
    employee = models.Employee.objects.filter(room__icontains=room)
    ser = serializers.EmployeeSerializer(employee)
    return Response(ser.data)



@api_view(["GET"])
def patient_by_doctor(request):
    doctor = request.GET.get("doctor")
    patient = models.Patients.objects.filter(doctor__icontains=doctor)
    ser = serializers.PatientsSerializer(patient)
    return Response(ser.data)


@api_view(["GET"])
def patient_by_full_name(request):
    full_name = request.GET.get("full_name")
    patient = models.Patients.objects.filter(full_name_icontains=full_name)
    ser = serializers.PatientsSerializer(patient)
    return Response(ser.data)


@api_view(["GET"])
def patient_by_gander(request):
    gander = request.GET.get("gander")
    patient = models.Patients.objects.filter(gander__icontains=gander)
    ser = serializers.PatientsSerializer(patient)
    return Response(ser.data)


@api_view(["GET"])
def patient_by_phone_number(request):
    phone_number = request.GET.get("phone_number")
    patient = models.Patients.objects.filter(phone_number=phone_number)
    ser = serializers.PatientsSerializer(patient)
    return Response(ser.data)


@api_view(["GET"])
def patient_by_room(request):
    room = request.GET.get("room")
    patient = models.Patients.objects.filter(room=room)
    ser = serializers.PatientsSerializer(patient)
    return Response(ser.data)


@api_view(["GET"])
def patient_by_payment_status(request):
    payment_status = request.GET.get("payment_status")
    patient = models.Patients.objects.filter(payment_status=payment_status)
    ser = serializers.PatientsSerializer(patient)
    return Response(ser.data)


@api_view(["GET"])
def room_by_name(request):
    name = request.GET.get("name")
    room = models.Room.objects.filter(name=name)
    ser = serializers.RoomSerializer(room)
    return Response(ser.data)


@api_view(["GET"])
def room_by_department(request):
    department = request.GET.get("department")
    room = models.Room.objects.filter(department=department)
    ser = serializers.RoomSerializer(room)
    return Response(ser.data)


@api_view(["GET"])
def room_by_capacity(request):
    capacity = request.GET.get("capacity")
    room = models.Room.objects.filter(capacity=capacity)
    ser = serializers.RoomSerializer(room)
    return Response(ser.data)

@api_view(["GET"])
def room_by_status(request):
    status = request.GET.get("status")
    room = models.Room.objects.filter(status=status)
    ser = serializers.RoomSerializer(room)
    return Response(ser.data)



@api_view(["GET"])
def room_by_is_booked(request):
    is_booked = request.GET.get("is_booked")
    room = models.Room.objects.filter(is_booked=is_booked)
    ser = serializers.RoomSerializer(room)
    return Response(ser.data)


@api_view(["GET"])
def room_by_equipment(request):
    equipment = request.GET.get("equipment")
    room = models.Room.objects.filter(equipment=equipment)
    ser = serializers.RoomSerializer(room)
    return Response(ser.data)








