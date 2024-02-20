from . import models
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = "__all__"

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Equipment
        fields = "__all__"

class Work_with_operationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Work_with_operations
        fields = "__all__"


class Clinical_statisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Clinical_statistics
        fields = "__all__"

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payment
        fields = "__all__"

class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patients
        fields = "__all__"


class Patient_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient_info
        fields = "__all__"

class AchievmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Achievements
        fields = "__all__"

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Income
        fields = "__all__"

class Incoming_incomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Incoming_income
        fields = "__all__"

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Devices
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = "__all__"

class Info_about_clinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Info_about_clinic
        fields = "__all__"
