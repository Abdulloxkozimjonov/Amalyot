from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from . import models

@admin.register(models.User)
class UserAdmin(UserAdmin):
    list_display = ['id','username', 'first_name', 'last_name', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ('gender','phone_number','img','bio','birthday','month_of_birth','born_smelly')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(models.Employee)
admin.site.register(models.Room)
admin.site.register(models.Income)
admin.site.register(models.Payment)
admin.site.register(models.Patients)
admin.site.register(models.Patient_info)
admin.site.register(models.Clinical_statistics)
admin.site.register(models.Department)
admin.site.register(models.Devices)
admin.site.register(models.Outgoing_income)
admin.site.register(models.Incoming_income)
admin.site.register(models.Work_with_operations)
admin.site.register(models.Achievements)
admin.site.register(models.Cassa)
admin.site.register(models.Comment)
admin.site.register(models.Info_about_clinic)
admin.site.register(models.Equipment)


