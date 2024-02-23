from django.urls import path
from . import views

urlpatterns = [
    path('filter-by-name/', views.employee_by_name),
    path('filter-by-age/', views.employee_by_age),
    path('filter-by-experience/', views.employee_by_experience)
]