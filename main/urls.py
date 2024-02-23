from django.urls import path
from . import views

urlpatterns = [
    path('filter_by_age/', views.employ_by_age)
]