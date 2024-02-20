from django.urls import path
from . import views

urlpatterns = [
 # Start Employee url
    path('create-employee/', views.CreateEmployee.as_view()),
    path('update-employee/', views.UpdateEmployee.as_view()),
    path('delete-employee/', views.DeleteEmployee.as_view()),
# End Employee url

# Start Room url
    path('create-room/', views.CreateRoom.as_view()),
    path('update-room/', views.UpdateRoom.as_view()),
    path('delete-room/', views.DeleteRoom.as_view()),
# End Room url

# Start Department url
    path('create-department/', views.CreateDepartment.as_view()),
    path('update-department/', views.UpdateDepartment.as_view()),
    path('delete-department/', views.DeleteDepartment.as_view()),
# End Department url

# Start Equpment url
    path('create-equpment/', views.CreateEqupment.as_view()),
    path('update-equpment/', views.UpdateEqupment.as_view()),
    path('delete-equpment/', views.DeleteEqupment.as_view()),
# End Equpment url

# Start Work_with_operations url
    path('create-equpment/', views.CreateWork_with_operations.as_view()),
    path('update-equpment/', views.UpdateWork_with_operations.as_view()),
    path('delete-equpment/', views.DeleteWork_with_operations.as_view()),
# End Work_with_operations url

# Start Clinical_statistics url
    path('create-equpment/', views.CreateEqupment.as_view()),
    path('update-equpment/', views.UpdateEqupment.as_view()),
    path('delete-equpment/', views.DeleteEqupment.as_view()),
# End Clinical_statistics url
]