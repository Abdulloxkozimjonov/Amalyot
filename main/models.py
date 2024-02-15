from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):
    GENDER=(
        ('Erkak', "Erkak"),
        ('Ayol', "Ayol")
    )
    gender = models.CharField(max_length=55, choices=GENDER, blank=False)
    phone_number = models.CharField(max_length=13, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    img= models.ImageField(upload_to='user-imgages/', validators=[
        RegexValidator(
            regex='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
            message='Invalide img ',
            code='Invalid photos'
        )
    ])
    bio = models.CharField(max_length=255)
    birthday = models.DateField()
    month_of_birth = models.DateField()
    born_smelly = models.DateField()


class Employee(models.Model):
    user = models.ForeignKey(to= 'User', on_delete=models.PROTECT)
    experience= models.CharField(max_length=255)
    age = models.IntegerField(default=18)
    POSITION=(
        ('Director', "director"),
    )
    position = models.CharField(max_length=255, choices=POSITION)
    salary = models.DecimalField(max_digits=10, decimal_places =2)
    room = models.ForeignKey(to= 'Room', on_delete=models.PROTECT)


class Room(models.Model):
    department = models.ForeignKey(to='Department', on_delete=models.CASCADE)
    room_type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    equipment = models.ForeignKey(to = 'Equipment', on_delete=models.PROTECT)


class Department(models.Model):
    name = models.CharField(max_length=255)


class Equipment(models.Model):
    name = models.CharField(max_length=55)