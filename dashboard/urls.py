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
]