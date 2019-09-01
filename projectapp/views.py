from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, redirect
from.models import department, faculty, projectCategory, thesisCategory, project, thesis, supervisor, internship, student
from django.contrib.auth import authenticate, login, logout
# from django.http import JsonResponse
from django.core import serializers
# Create your views here.
#Combobox data
import json
from django.utils.dateparse import parse_date
from django.core.files.storage import FileSystemStorage



def index(request):
    department_data = department.objects.all()
    context={
        "d_Data":department_data
    }
    return render(request, "index.html",context)

def getallproject(request):
    project_data = project.objects.all()
    context={
        "p_data":project_data
    }
    return render(request, "allproject.html", context)

def getallthesis(request):
    thesis_data = thesis.objects.all()
    context={
        "t_data":thesis_data
    }
    return render(request, "allthesis.html", context)

def getallinternship(request):
    internship_data = internship.objects.all()
    context={
        "i_data":internship_data
    }
    return render(request, "allinternship.html", context)

def getallfaculty(request):
   faculty_data = faculty.objects.all()
   department_data = department.objects.all()
   context={
       "f_data":faculty_data,
       "d_data":department_data
   }
   return render(request, "faculty.html", context)

def getqueryprojects(request, id):
    department_data = get_object_or_404(department, id=id)
    project_data = projectCategory.objects.filter(department = department_data.id)
    
    context={
        "p_data": project_data
    }

    return render(request, "queryproject.html", context)

def getquerythesis(request, id):
    department_data = get_object_or_404(department, id=id)
    thesis_data = thesisCategory.objects.filter(department = department_data.id)
    context={
        "t_data":thesis_data
    }
    return render(request, "querythesis.html", context)


def getqueryprojectslist(request, id):
    c_data = get_object_or_404(projectCategory, id=id)
    project_data = project.objects.filter(project_category = c_data.id)
    context={
        "p_data": project_data
    }

    return render(request, "queryprojectlist.html", context)

def getquerythesislist(request, id):
    c_data = get_object_or_404(thesisCategory, id=id)
    thesis_data = thesis.objects.filter(thesis_category = c_data.id)
    context={
        "t_data": thesis_data
    }

    return render(request, "querythesislist.html", context)

def getqueryinternshiplist(request, id):
    department_data = get_object_or_404(department, id=id)
    intern_data = internship.objects.filter(department = department_data.id)
    context={
        "i_data": intern_data
    }

    return render(request, "queryinternshiplist.html", context)

def supervisors(request):
    supervisors_data = supervisor.objects.all()
    context={
        "s_data":supervisors_data
    }
    return render(request, "supervisors.html", context)

def getLogin(request):


    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=username, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('index')
   
    return render(request, "pages-sign-in.html")

def getLogout(request):
    logout(request)
    return redirect('index')


def test(request):
   
    return render(request, "dashboard.html")

def PageNotFound(request):
   
    return render(request, "pages-404.html")

#Add Project Combobox data

def addProjectData(request):
    
    faculties = faculty.objects.all()
    department_data = department.objects.all()
    supervisor_data = supervisor.objects.all()
    projectCategory_data = projectCategory.objects.all()
    context={
        "f_data":faculties,
        "d_data":department_data,
        "s_data":supervisor_data,
        "pCategory_data":projectCategory_data,
    }

    if request.method=="POST":
        projectNo = request.POST.get('projectNo')
        projectTitle = request.POST.get('projectTitle')
        projectDetails = request.POST.get('projectDetails')
        projectFile = request.FILES['projectFile']
        projectReport = request.FILES['projectReport']
        facultyCombobox = request.POST.get('facultyCombobox')
        departmentCombobox = request.POST.get('departmentCombobox')
        supervisorCombobox = request.POST.get('supervisorCombobox')
        projectCategoryCombobox = request.POST.get('projectCategoryCombobox')
        date = request.POST.get('date')

        # print(projectFile.name)
        # print(projectFile.size)
        fs = FileSystemStorage()


        facultyId = faculty.objects.get(id=facultyCombobox)
        departmentId = department.objects.get(id=departmentCombobox)
        supervisorId = supervisor.objects.get(id=supervisorCombobox)
        projectCategoryId = projectCategory.objects.get(id=projectCategoryCombobox)

        tempDate = parse_date(date)

        NewProject = project(
            project_no = projectNo,
            project_title = projectTitle,
            project_details = projectDetails,
            project_file = fs.save('project/file/' + projectFile.name, projectFile),
            project_report = fs.save('project/report/' + projectReport.name, projectReport),
            faculty = facultyId,
            department = departmentId,
            supervisor = supervisorId,
            project_category = projectCategoryId,
            submission_date = tempDate
        )
        NewProject.save();

        

        return redirect('/add-projects')
    return render(request, 'add-projects-form.html', context)


def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'pages-404.html', data)



















# def get_data(request, *args, **kwargs):
#     department_data = get_object_or_404(department, id=1)
#     data = projectCategory.objects.filter(department = department_data.id)
#     #data = projectCategory.objects.all()
#     posts_serialized = serializers.serialize('json', data)
#     return JsonResponse(posts_serialized, safe=False)
# def get_data(reques, *args, **kwargs):
#     c_data = get_object_or_404(projectCategory, id=1)
#     project_data = project.objects.filter(project_category = c_data.id).count()
#     data={
#         "Web Basedaccha , a": project_data,
#         "customer": 20,
#     }
#     return JsonResponse(data)

