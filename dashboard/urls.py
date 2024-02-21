from django.urls import path
from . import views

urlpatterns = [
 # Start Employee url
    path('create-employee/', views.CreateEmployee.as_view()),
    path('update-employee/<int:pk>/', views.UpdateEmployee.as_view()),
    path('delete-employee/<int:pk>/', views.DeleteEmployee.as_view()),
# End Employee url

# Start Room url
    path('create-room/', views.CreateRoom.as_view()),
    path('update-room/<int:pk>/', views.UpdateRoom.as_view()),
    path('delete-room/<int:pk>/', views.DeleteRoom.as_view()),
# End Room url

# Start Department url
    path('create-department/', views.CreateDepartment.as_view()),
    path('update-department/<int:pk>/', views.UpdateDepartment.as_view()),
    path('delete-department/<int:pk>/', views.DeleteDepartment.as_view()),
# End Department url

# Start Equpment url
    path('create-equpment/', views.CreateEqupment.as_view()),
    path('update-equpment/<int:pk>/', views.UpdateEqupment.as_view()),
    path('delete-equpment/<int:pk>/', views.DeleteEqupment.as_view()),
# End Equpment url

# Start Work_with_operations url
    path('create-work_with_operations/', views.CreateWork_with_operations.as_view()),
    path('update-work_with_operations/<int:pk>/', views.UpdateWork_with_operations.as_view()),
    path('delete-work_with_operations/<int:pk>/', views.DeleteWork_with_operations.as_view()),
# End Work_with_operations url

# Start Clinical_statistics url
    path('create-clinical_statistics/', views.CreateClinical_statistics.as_view()),
    path('update-clinical_statistics/<int:pk>/', views.UpdateClinical_statistics.as_view()),
    path('delete-clinical_statistics/<int:pk>/', views.DeleteClinical_statistics.as_view()),
# End Clinical_statistics url

# Start Payment url
    path('create-payment/', views.CreatePayment.as_view()),
    path('update-payment/<int:pk>/', views.UpdatePayment.as_view()),
    path('delete-payment/<int:pk>/', views.DeletePayment.as_view()),
# End Payment url

# Start Attendance url
    path('create-attendance/', views.CreateAttendance.as_view()),
# End Attendance url

# Start Income url
    path('create-income/', views.CreateIncome.as_view()),
    path('update-income/<int:pk>/', views.UpdateIncome.as_view()),
    path('delete-income/<int:pk>/', views.DeleteIncome.as_view()),
# End Income url

# Start Patients url
    path('create-patients/', views.CreatePatients.as_view()),
    path('update-patients/<int:pk>/', views.UpdatePatients.as_view()),
    path('delete-patients/<int:pk>/', views.DeletePatients.as_view()),
# End Patients url

# Start Patient_info url
    path('create-patient_info/', views.CreatePatient_info.as_view()),
    path('update-patient_info/<int:pk>/', views.UpdatePatient_info.as_view()),
    path('delete-patient_info/<int:pk>/', views.DeletePatient_info.as_view()),
# End Patient_info url

# Start Devices url
    path('create-devices/', views.CreateDevices.as_view()),
    path('update-devices/<int:pk>/', views.UpdateDevices.as_view()),
    path('delete-devices/<int:pk>/', views.DeleteDevices.as_view()),
# End Injury url

# Start Injury url
    path('create-injury/', views.CreateInjury.as_view()),
    path('update-injury/<int:pk>/', views.UpdateInjury.as_view()),
    path('delete-injury/<int:pk>/', views.DeleteInjury.as_view()),
# End Injury url
]