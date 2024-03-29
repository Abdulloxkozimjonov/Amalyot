from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
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

    class Meta(AbstractUser.Meta):
        swappable= 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'



class Employee(models.Model):
    user = models.ForeignKey(to= 'User', on_delete=models.PROTECT)
    full_name = models.CharField(max_length= 255, blank = False)
    experience= models.CharField(max_length=255)
    age = models.IntegerField(default=18)
    status  = models.CharField(max_length = 255)
    POSITION=(
        ('Director', "director"),
        ('Manager', "manager"),
        ('Doctor', "doctor"),
        ('Hamshira', "hamshira"),

    )
    position = models.CharField(max_length=255, choices=POSITION)
    salary = models.DecimalField(max_digits=10, decimal_places =2)
    room = models.ForeignKey(to= 'Room', on_delete=models.PROTECT)
    work_time = models.TimeField()
    dapartment = models.ForeignKey(to= 'Department', on_delete = models.CASCADE)


class Room(models.Model):
    department = models.ForeignKey(to='Department', on_delete=models.CASCADE)
    room_type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    equipment = models.ForeignKey(to = 'Equipment', on_delete=models.PROTECT)
    capacity = models.CharField(max_length= 255)
    status = models.CharField(max_length = 255)
    is_booked = models.BooleanField(default = False)


class Department(models.Model):
    name = models.CharField(max_length=255)


class Equipment(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=55)
    type = models.CharField(max_length=255)


class Work_with_operations(models.Model):
    name = models.CharField(max_length=100)
    employee = models.ForeignKey(to='Employee', on_delete=models.CASCADE)
    patient = models.ForeignKey(to='Patient', on_delete=models.CASCADE)
    room = models.ForeignKey(to='Room', on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    cost = models.PositiveIntegerField()
    date_time = models.DateTimeField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_number = models.ForeignKey(to='Room', on_delete=models.CASCADE)


class Clinical_statistics(models.Model):
    achievements = models.ForeignKey(to='achievements', on_delete=models.CASCADE)


class Payment(models.Model):
    patient = models.ForeignKey(to='Patient', on_delete= models.CASCADE)
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    PAYMENT_TYPE=(
        ('Nakd pull', 'Nakd pull'),
        ('Karta orqali','Karta orqali')
    )
    payment_type = models.CharField(max_length=255, choices=PAYMENT_TYPE )
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_day = models.DateField()
    date = models.DateField()
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now = True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=4,
        )
        qr.add_data(f"Your data to encode in the QR code: {self.payment_day}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

        super().save(*args, **kwargs)

        def __str__(self):
            return self.payment_day


class Patients(models.Model):
    full_name = models.CharField(max_length = 255, blank = False)
    doctor = models.ForeignKey(to='User', on_delete=models.CASCADE)
    GENDER = (
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol')
    )
    gander = models.CharField(max_length = 100, choices = GENDER, blank = False)
    phone_number = models.CharField(max_length=100, validators = [
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    room = models.ForeignKey(to='Room', on_delete = models.CASCADE)
    complaint = models.CharField(max_length=100)
    Suggestions = models.CharField(max_length=100)
    comments = models.CharField(max_length=100)
    PAYMENT_STATUS = (
        ('1', 'Naqt pull'),
        ('2', 'Karta orqali'),
    )
    payment_status = models.IntegerField(choices = PAYMENT_STATUS)

class Patient_info(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    GENDER = (
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol')
    )
    gender = models.CharField(max_length=100, choices=GENDER)
    phone_nummber = models.CharField(max_length=13, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])

class Achievements(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='Achievements-img/', validators=[
        RegexValidator(
            regex='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
            message='Invalide img ',
            code='Invalid photos'
        )
    ])


class Income(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.PROTECT)
    day = models.DateField()
    date = models.DateField(auto_now = True)
    amount = models.PositiveIntegerField()
    gross_profit = models.PositiveIntegerField()
    outgoing_income = models.ForeignKey(to='Outgoing_income', on_delete=models.PROTECT)
    incoming_revenue = models.ForeignKey(to='Incoming_income', on_delete=models.PROTECT)

class Outgoing_income(models.Model):
    amount = models.PositiveIntegerField()
    Outgoing_income = models.IntegerField()
    bio = models.CharField(max_length=100)


class Incoming_income(models.Model):
    amount = models.PositiveIntegerField()
    Incoming_income = models.IntegerField()
    bio = models.CharField(max_length=100)


class Devices(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    room = models.ForeignKey(to='Room', on_delete=models.PROTECT)


class Cassa(models.Model):
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)


class Comment(models.Model):
    patient = models.ForeignKey(to='Patients', on_delete=models.CASCADE)
    comment = models.TextField()
    status = models.CharField(max_length= 255)
    created_at = models.DateTimeField(auto_created=True)


class Info_about_clinic(models.Model):
    total_patients_number = models.IntegerField()
    total_employee_number = models.IntegerField()
    bio = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])


class Injury(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)


class Attendance(models.Model):
    employee = models.ForeignKey(to='Employee', on_delete=models.CASCADE)
    date = models.DateField()
    chek_in = models.TimeField(null=True, blank=True)
    chek_out = models.TimeField(null=True, blank=True)

    class Meta:
        unique_together = ['employee', 'date']

    def clean(self):
        if self.chek_out and self.chek_out < self.chek_in:
            raise ValidationError('Check-out time must be after chek-in time.')

    def str(self):
        return f'{self.employee.full_name} - {self.date}'




