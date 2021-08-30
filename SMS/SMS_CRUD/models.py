from django.db import models

# Create your models here.

import os 
class School(models.Model):
    School_Name = models.CharField(max_length=100)

    def __str__(self):
        return self.School_Name


class Teacher(models.Model):
    School_Name = models.ForeignKey(School, on_delete=models.CASCADE)
    Teacher_Name = models.CharField(max_length=100)
    Teacher_Address = models.TextField()
    Teacher_Joining_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.Teacher_Name)

class Student(models.Model):
    School_Name = models.ForeignKey(School, on_delete=models.CASCADE,null=True,blank=True)
    Teacher_Name = models.ForeignKey(Teacher, on_delete=models.CASCADE,null=True,blank=True)
    Student_Name = models.CharField(max_length=100,null=True,blank=True)
    Student_Address = models.TextField(null=True,blank=True)
    Student_Roll_No = models.IntegerField(null=True,blank=True)
    Student_File = models.FileField(upload_to='pdf',null=True,blank=True)

    def __str__(self):
        return "{}".format(self.Student_Name)



