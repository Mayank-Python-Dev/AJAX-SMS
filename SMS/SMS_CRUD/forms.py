from django import forms

from .models import *


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['School_Name','Teacher_Name','Student_Name','Student_Address','Student_Roll_No']

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['Student_File']