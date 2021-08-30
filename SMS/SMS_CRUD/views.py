from django.shortcuts import render , redirect

# Create your views here.
from .models import *

from .forms import *

from django.http import JsonResponse

# from django.views.decorators.csrf import csrf_exempt

from django.conf import settings


def home(request):
    form = StudentRegistration()
    getStudent = Student.objects.all()
    context = {'getStudent': getStudent, 'form': form}
    return render(request, 'SMS_CRUD/home.html', context)


def student_data(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            getstudentID = request.POST.get('studid')
            School_Name = int(request.POST['School_Name'])
            Teacher_Name= int(request.POST['Teacher_Name'])
            Student_Name = request.POST['Student_Name']
            Student_Address = request.POST['Student_Address']
            Student_Roll_No = request.POST['Student_Roll_No']
            if getstudentID == '':
                getAllData = Student(School_Name_id=School_Name,Teacher_Name_id=Teacher_Name,Student_Name=Student_Name,Student_Address=Student_Address,Student_Roll_No=Student_Roll_No)
            else:
                getAllData = Student(id = getstudentID,School_Name_id=School_Name,Teacher_Name_id=Teacher_Name,Student_Name=Student_Name,Student_Address=Student_Address,Student_Roll_No=Student_Roll_No)
            
            getAllData.save()
            getStudentData = Student.objects.values('id','School_Name__School_Name','Teacher_Name__Teacher_Name','Teacher_Name__Teacher_Name','Student_Name','Student_Address','Student_Roll_No','Student_File')
            studentList = list(getStudentData)
            print(studentList)
            return JsonResponse({'status':'save','studentList':studentList})
        else:
            return JsonResponse({'status':0})

# @csrf_exempt
def delete_student_data(request):
    if request.method == "POST":
        getid = request.POST.get('sid')
        print(getid)
        getData = Student.objects.get(id=getid)
        getData.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status':0})


def edit_student_data(request):
    if request.method == "POST":
        getid = request.POST.get('sid')
        print(getid)
        getData = Student.objects.get(id=getid)
        print(getData.Student_File.url)
        Obj1 = {"id":getData.id, "school_name": getData.School_Name.id, "teacher_name" : getData.Teacher_Name.id, "student_name" :getData.Student_Name,"student_address" :getData.Student_Address,"student_rollno":getData.Student_Roll_No}
        # print(Obj1)
        return JsonResponse(Obj1)



def upload_file(request,pk):
    getID = Student.objects.get(id=pk)
    print(getID.School_Name)
    form = StudentRegistrationForm()
    if request.method == "POST":
        form = StudentRegistrationForm(request.FILES)
        if form.is_valid():
            getID.Student_File = request.FILES.get('Student_File')
            getID.save()
    context = {'form':form,'getID' : getID}
    return render(request,'SMS_CRUD/fileupload.html',context)


def download(request, pk):
    obj = Student.objects.get(id=pk)
    print(obj.Student_File)
    file_path = settings.MEDIA_ROOT + obj.Student_File
    file_wrapper = FileWrapper(file(file_path,'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    response = HttpResponse(file_wrapper, content_type=file_mimetype )
    response['X-Sendfile'] = file_path
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = 'attachment; filename=%s/' % smart_str(file_name) 
    return response