from django.urls import path
from . import views

urlpatterns = [
    # ------------EMPLOYEE-----------------
    path('filter_employee_by_age/', views.employ_by_age),
    path('filter_employee_by_full_name/', views.employ_by_full_name),
    path('filter_employee_by_status/', views.employ_by_status),
    path('filter_employee_by_work_time/', views.employ_by_work_time),
    path('filter_employee_by_experience/', views.employ_by_experience),
    path('filter_employee_by_department/', views.employ_by_department),
    path('filter_employee_by_salary/', views.employ_by_salary),
    path('filter_employee_by_room/', views.employ_by_room),
    path('filter_employee_by_work_time/', views.employ_by_work_time),
     # ----------------PATIENT---------------
    path('filter_patient_by_doctor/', views.patient_by_doctor),
    path('filter_patient_by_gander/', views.patient_by_gander),
    path('filter_patient_by_phone_number/', views.patient_by_phone_number),
    path('filter_patient_by_room/', views.patient_by_room),
    path('filter_patient_by_payment_status/', views.patient_by_payment_status),
    # ----------------ROOM------------------
    path('filter_room_by_name/', views.room_by_name),
    path('filter_room_by_department/', views.room_by_department),
    path('filter_room_by_capacity/', views.room_by_capacity),
    path('filter_room_by_status/', views.room_by_status),
    path('filter_room_by_is_booked/', views.room_by_is_booked),
    path('filter_room_by_equipment/', views.room_by_equipment),
    # --------------PAYMENT------------
    path('filter_payment_by_patient/', views.payment_by_patient),
    path('filter_payment_by_created_at/', views.payment_by_created_at),
    path('filter_payment_by_payment_type/', views.payment_by_payment_type),
    # --------------COMMENT---------
    path('filter_comment_by_status/', views.comment_by_status),
    # -----------INCOME----------
    path('filter_income_by_date/', views.income_by_date),
    path('filter_income_by_amount/', views.income_by_amount),
    # ---------------RAVENUE-----------
    path('filter_ravenue_by_date/', views.ravenue_by_date),
    path('filter_ravenue_by_amount/', views.ravenue_by_amount),
    # ----------OPERATION----------
    path('filter_operation_by_employee/', views.operation_by_employee),
    path('filter_operation_by_date_time/', views.operation_by_date_time),
    path('filter_operation_by_start_time/', views.operation_by_start_time),
    path('filter_operation_by_end_time/', views.operation_by_en_time),
    path('filter_operation_by_patient/', views.operation_by_patient),
    path('filter_operation_by_room/', views.operation_by_room),
    # -----------EQUIPMENT--------
    path('filter_equipment_by_name/', views.equipment_by_name),
    # -----------DEPARTMENT-----------
    path('filter_department_by_name/', views.department_by_name),
    # -------------ATTENDANCE-----------
    path('filter_attendance_by_employee/', views.attendance_by_employee),
    path('filter_attendance_by_date/', views.attendance_by_date),


]