from django.contrib import admin
from django.db.models import fields

# Register your models here.

from .models import *


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['School_Name']

    def has_delete_permission(self, request, obj=None):
        #Disable delete
        return False


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['School_Name', 'Teacher_Name','Teacher_Address', 'Teacher_Joining_Date']
    list_filter = ('School_Name', 'Teacher_Name','Teacher_Address', 'Teacher_Joining_Date')

    def has_delete_permission(self, request, obj=None):
        #Disable delete
        return False


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['School_Name', 'Teacher_Name',
                        'Student_Name', 'Student_Address', 'Student_Roll_No', 'Student_File']
    list_filter = ('School_Name_id', 'Teacher_Name',
                        'Student_Name', 'Student_Address', 'Student_Roll_No', 'Student_File')


    def has_delete_permission(self, request, obj=None):
        #Disable delete
        return False

# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == "Teacher_Name":
#             kwargs["queryset"] = School.objects.filter(
#                 School_Name='Jayshree Periwal')
#             kwargs["queryset"] = Student.objects.filter(
#                 School_Name__School_Name=list(kwargs["queryset"]))
#             print(kwargs['queryset'])
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)
#     list_display = ['School_Name', 'Teacher_Name',
#                     'Student_Name', 'Student_Address', 'Student_Roll_No', 'Student_File']
