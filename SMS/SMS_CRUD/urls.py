from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('savingStudentData/',views.student_data,name='save'),
    path('deleteStudentData/',views.delete_student_data,name = 'delete'),
    path('editStudentData/',views.edit_student_data,name = 'edit'),
    path('uploadFile/<str:pk>/',views.upload_file,name='upload'),
    path('downloadFile/<str:pk>/',views.download,name='download'),

]
