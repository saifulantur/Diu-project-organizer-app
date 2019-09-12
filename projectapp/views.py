from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, redirect
from.models import adminprofile,department, faculty, projectCategory, thesisCategory, project, thesis, supervisor, internship, questionAndAnswer
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.core import serializers
# Create your views here.
#Combobox data
import json
from django.utils.dateparse import parse_date
from django.core.files.storage import FileSystemStorage
from .forms import ProjectForm, SupervisorForm, ProjectCategoryForm, ThesisCategoryForm, ThesisFrom, InternshipForm, QnAForm
from django.contrib.auth.decorators import login_required


dId = 0
tId = 0
def index(request):
    # userName = request.user.username
    return render(request, "index.html")

def getallproject(request):
    project_data = project.objects.all()
    countProjectData = project_data.count()
    context={
        "p_data":project_data,
        "count": countProjectData
    }
    return render(request, "allproject.html", context)

def getallthesis(request):
    thesis_data = thesis.objects.all()
    countThesisData = thesis_data.count()
    context={
        "t_data":thesis_data,
        "count": countThesisData
    }
    return render(request, "allthesis.html", context)

def getallinternship(request):
    internship_data = internship.objects.all()
    countInternshipData = internship_data.count()
    context={
        "i_data":internship_data,
        "count": countInternshipData
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

    global dId
    dId=id
    # print(dId)
    context={
        "p_data": project_data,
        
    }

    return render(request, "queryproject.html", context)

#Start Project Category Graph
def getProjectCategoryData(request, *args, **kwargs):
    global dId
    # print(dId)
    department_data = get_object_or_404(department, id=dId)
    project_data = projectCategory.objects.filter(department = department_data.id)
    
    projectData = project.objects.all()
    ProjectCategorylabels = []
    ProjectCategorylistData = []
    for i in project_data:
        ProjectCategorylabels.append(i.category_project)
        projectData = project.objects.filter(project_category_id = i.id)
        row_count=projectData.count()
        ProjectCategorylistData.append(row_count)
    # print(project_data)
    data = {
        "labels": ProjectCategorylabels,
        "defaultData": ProjectCategorylistData
    }
    return JsonResponse(data)
#End Project Category Graph

def getquerythesis(request, id):
    department_data = get_object_or_404(department, id=id)
    thesis_data = thesisCategory.objects.filter(department = department_data.id)
    global tId
    tId=id
    # print(tId)
    context={
        "t_data":thesis_data
    }
    return render(request, "querythesis.html", context)


#Start Thesis Category Graph
def getThesisCategoryData(request, *args, **kwargs):
    global tId
    # print(tId)
    department_data = get_object_or_404(department, id=tId)
    thesis_data = thesisCategory.objects.filter(department = department_data.id)
    
    thesisData = thesis.objects.all()
    thesisCategorylabels = []
    thesisCategorylistData = []
    for i in thesis_data: 
        thesisCategorylabels.append(i.category_thesis)
        thesisData = thesis.objects.filter(thesis_category_id = i.id)
        row_count=thesisData.count()
        thesisCategorylistData.append(row_count)
    # print(thesis_data)
    data = {
        "labels": thesisCategorylabels,
        "defaultData": thesisCategorylistData
    }
    return JsonResponse(data)
#End Thesis Category Graph


def getqueryprojectslist(request, id):
    c_data = get_object_or_404(projectCategory, id=id)
    project_data = project.objects.filter(project_category = c_data.id)
    # print(c_data)
    row_count=project_data.count()
    context={
        "p_data": project_data,
        "count": row_count,
        "projectCategoryName": c_data
    }

    return render(request, "queryprojectlist.html", context)

def getquerythesislist(request, id):
    c_data = get_object_or_404(thesisCategory, id=id)
    thesis_data = thesis.objects.filter(thesis_category = c_data.id)
    row_count=thesis_data.count()

    context={
        "t_data": thesis_data,
        "count": row_count,
        "thesisCategoryName": c_data

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

def getQuestion(request):
    QnAData = questionAndAnswer.objects.all()
    context = {
        "q_data":QnAData
    }
    return render(request, "QnA.html", context)

def PageNotFound(request):
   
    return render(request, "pages-404.html")

def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'pages-404.html', data)

#Add Project Form data

@login_required()
def getCreate(request):
    form =  ProjectForm(request.POST or None, request.FILES or None)
    postedById = adminprofile.objects.get(user = request.user.id)

    #combobox data query
    faculties = faculty.objects.all()
    department_data = department.objects.all()
    supervisor_data = supervisor.objects.all()
    projectCategory_data = projectCategory.objects.all()
    #table data query
    check_id = request.user.id
    adminProfile_user = get_object_or_404(adminprofile, user=check_id)
    posted_by_id = adminProfile_user.id
    project_data_for_table = project.objects.filter(posted_by = posted_by_id)

    context ={
        "form":form,
        "project_data_for_table":project_data_for_table,
        "f_data":faculties,
        "d_data":department_data,
        "s_data":supervisor_data,
        "pCategory_data":projectCategory_data,
    }
    if request.user.is_authenticated:
        if request.method=="POST":
            facultyCombobox = request.POST.get('facultyCombobox')
            departmentCombobox = request.POST.get('departmentCombobox')
            supervisorCombobox = request.POST.get('supervisorCombobox')
            projectCategoryCombobox = request.POST.get('projectCategoryCombobox')

            #convert combobox data as a foreginkey 
            facultyId = faculty.objects.get(id=facultyCombobox)
            departmentId = department.objects.get(id=departmentCombobox)
            supervisorId = supervisor.objects.get(id=supervisorCombobox)
            projectCategoryId = projectCategory.objects.get(id=projectCategoryCombobox)
            postedById = adminprofile.objects.get(user = request.user.id)

            #get Student Information
            student_id_1 = request.POST.get('student_id_1')
            student_id_2 = request.POST.get('student_id_2')
            student_id_3 = request.POST.get('student_id_3')
            student_id_4 = request.POST.get('student_id_4')



            if form.is_valid():
                instance = form.save(commit=False)
                instance.faculty = facultyId
                instance.department = departmentId
                instance.supervisor = supervisorId
                instance.project_category = projectCategoryId
                instance.posted_by = postedById
                instance.student_id_1 = student_id_1
                instance.student_id_2 = student_id_2
                instance.student_id_3 = student_id_3
                instance.student_id_4 = student_id_4
                instance.save()
                return redirect('create')

    return render(request, 'addProject.html', context)


@login_required()
def getUpdate(request, id):
    postedById = adminprofile.objects.get(user = request.user.id)
    get_project_data = get_object_or_404(project, id=id)
    form =  ProjectForm(request.POST or None, request.FILES or None, instance=get_project_data)
    #combobox data query
    faculties = faculty.objects.all()
    department_data = department.objects.all()
    supervisor_data = supervisor.objects.all()
    projectCategory_data = projectCategory.objects.all()
    context ={
        "form":form,
        "projectData" : get_project_data,
        "f_data":faculties,
        "d_data":department_data,
        "s_data":supervisor_data,
        "pCategory_data":projectCategory_data,
    }
    # print(get_project_data.supervisor)
    if request.method=="POST":
        facultyCombobox = request.POST.get('facultyCombobox')
        departmentCombobox = request.POST.get('departmentCombobox')
        supervisorCombobox = request.POST.get('supervisorCombobox')
        projectCategoryCombobox = request.POST.get('projectCategoryCombobox')

        #get Student Information
        student_id_1 = request.POST.get('student_id_1')
        student_id_2 = request.POST.get('student_id_2')
        student_id_3 = request.POST.get('student_id_3')
        student_id_4 = request.POST.get('student_id_4')

        #convert combobox data as a foreginkey 
        facultyId = faculty.objects.get(id=facultyCombobox)
        departmentId = department.objects.get(id=departmentCombobox)
        supervisorId = supervisor.objects.get(id=supervisorCombobox)
        projectCategoryId = projectCategory.objects.get(id=projectCategoryCombobox)
        postedById = adminprofile.objects.get(user = request.user.id)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.faculty = facultyId
            instance.department = departmentId
            instance.supervisor = supervisorId
            instance.project_category = projectCategoryId
            instance.posted_by = postedById
            instance.student_id_1 = student_id_1
            instance.student_id_2 = student_id_2
            instance.student_id_3 = student_id_3
            instance.student_id_4 = student_id_4
            instance.save()
            return redirect('create')

    return render(request, 'addProject.html', context)

@login_required()
def getDelete(request, id):
    if request.user.is_authenticated:
        project_data = get_object_or_404(project, id=id)
        project_data.delete()
        return redirect('create')
    # return render(request, 'addProject.html')


# Supervisor Form Data
@login_required()
def getCreateSupervisor(request):
    form =  SupervisorForm(request.POST or None, request.FILES or None)
    postedById = adminprofile.objects.get(user = request.user.id)

    #combobox data query
    faculties = faculty.objects.all()
    department_data = department.objects.all()

    #table data query
    check_id = request.user.id
    adminProfile_user = get_object_or_404(adminprofile, user=check_id)
    posted_by_id = adminProfile_user.id
    supervisor_data_for_table = supervisor.objects.filter(posted_by = posted_by_id)

    context ={
        "form":form,
        "supervisor_data_for_table":supervisor_data_for_table,
        "f_data":faculties,
        "d_data":department_data,
    }
    if request.user.is_authenticated:
        if request.method=="POST":
            facultyCombobox = request.POST.get('facultyCombobox')
            departmentCombobox = request.POST.get('departmentCombobox')
    
            #convert combobox data as a foreginkey 
            facultyId = faculty.objects.get(id=facultyCombobox)
            departmentId = department.objects.get(id=departmentCombobox)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.faculty = facultyId
                instance.department = departmentId
                instance.posted_by = postedById
                instance.save()
                return redirect('createSupervisor')

    return render(request, 'addSupervisor.html', context)


@login_required()
def getUpdateSupervisor(request, id):
    postedById = adminprofile.objects.get(user = request.user.id)

    get_supervisor_data = get_object_or_404(supervisor, id=id)
    form =  SupervisorForm(request.POST or None, request.FILES or None, instance=get_supervisor_data)
    #combobox data query
    faculties = faculty.objects.all()
    department_data = department.objects.all()

    context ={
        "form":form,
        "f_data":faculties,
        "d_data":department_data,
        "supervisorData":get_supervisor_data
    }
    # print(get_project_data.supervisor)
    if request.method=="POST":
        facultyCombobox = request.POST.get('facultyCombobox')
        departmentCombobox = request.POST.get('departmentCombobox')

        #convert combobox data as a foreginkey 
        facultyId = faculty.objects.get(id=facultyCombobox)
        departmentId = department.objects.get(id=departmentCombobox)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.faculty = facultyId
            instance.department = departmentId
            instance.posted_by = postedById
            instance.save()
            return redirect('createSupervisor')


    return render(request, 'addSupervisor.html', context)

@login_required()
def getDeleteSupervisor(request, id):
    if request.user.is_authenticated:
        supervisor_data = get_object_or_404(supervisor, id=id)
        supervisor_data.delete()
        return redirect('createSupervisor')


# Project Category Form Data
@login_required()
def getCreateProjectCategory(request):

    form =  ProjectCategoryForm(request.POST or None, request.FILES or None)
    postedById = adminprofile.objects.get(user = request.user.id)

    #combobox data query
    department_data = department.objects.all()

    #table data query
    check_id = request.user.id
    adminProfile_user = get_object_or_404(adminprofile, user=check_id)
    posted_by_id = adminProfile_user.id
    project_category_data_for_table = projectCategory.objects.filter(posted_by = posted_by_id)

    context ={
        "form":form,
        "project_category_data_for_table":project_category_data_for_table,
        "d_data":department_data,
    }
    if request.user.is_authenticated:
        if request.method=="POST":
            departmentCombobox = request.POST.get('departmentCombobox')
    
            #convert combobox data as a foreginkey 
            departmentId = department.objects.get(id=departmentCombobox)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.department = departmentId
                instance.posted_by = postedById
                instance.save()
                return redirect('createProjectCategory')

    return render(request, 'addProjectCategory.html', context)


@login_required()
def getUpdateProjectCategory(request, id):

    postedById = adminprofile.objects.get(user = request.user.id)
    get_project_category_data = get_object_or_404(projectCategory, id=id)

    form =  ProjectCategoryForm(request.POST or None, request.FILES or None, instance=get_project_category_data)
    #combobox data query
    department_data = department.objects.all()

    context ={
        "form":form,
        "d_data":department_data,
        "get_project_category_data":get_project_category_data
    }
    if request.method=="POST":
        departmentCombobox = request.POST.get('departmentCombobox')

        #convert combobox data as a foreginkey 
        departmentId = department.objects.get(id=departmentCombobox)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.department = departmentId
            instance.posted_by = postedById
            instance.save()
            return redirect('createProjectCategory')

    return render(request, 'addProjectCategory.html', context)


@login_required()
def getDeleteProjectCategory(request, id):
    if request.user.is_authenticated:
        project_category_data = get_object_or_404(projectCategory, id=id)
        project_category_data.delete()
        return redirect('createProjectCategory')


# Thesis Category Form Data
@login_required()
def getCreateThesisCategory(request):

    form =  ThesisCategoryForm(request.POST or None, request.FILES or None)
    postedById = adminprofile.objects.get(user = request.user.id)

    #combobox data query
    department_data = department.objects.all()

    #table data query
    check_id = request.user.id
    adminProfile_user = get_object_or_404(adminprofile, user=check_id)
    posted_by_id = adminProfile_user.id
    thesis_category_data_for_table = thesisCategory.objects.filter(posted_by = posted_by_id)

    context ={
        "form":form,
        "thesis_category_data_for_table":thesis_category_data_for_table,
        "d_data":department_data,
    }
    if request.user.is_authenticated:
        if request.method=="POST":
            departmentCombobox = request.POST.get('departmentCombobox')
    
            #convert combobox data as a foreginkey 
            departmentId = department.objects.get(id=departmentCombobox)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.department = departmentId
                instance.posted_by = postedById
                instance.save()
                return redirect('createThesisCategory')

    return render(request, 'addThesisCategory.html', context)


@login_required()
def getUpdateThesisCategory(request, id):

    postedById = adminprofile.objects.get(user = request.user.id)
    get_thesis_category_data = get_object_or_404(thesisCategory, id=id)

    form =  ThesisCategoryForm(request.POST or None, request.FILES or None, instance=get_thesis_category_data)
    #combobox data query
    department_data = department.objects.all()

    context ={
        "form":form,
        "d_data":department_data,
        "get_thesis_category_data":get_thesis_category_data
    }
    if request.method=="POST":
        departmentCombobox = request.POST.get('departmentCombobox')

        #convert combobox data as a foreginkey 
        departmentId = department.objects.get(id=departmentCombobox)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.department = departmentId
            instance.posted_by = postedById
            instance.save()
            return redirect('createThesisCategory')

    return render(request, 'addThesisCategory.html', context)


@login_required()
def getDeleteThesisCategory(request, id):
    if request.user.is_authenticated:
        thesis_category_data = get_object_or_404(thesisCategory, id=id)
        thesis_category_data.delete()
        return redirect('createThesisCategory')


# Thesis Form Data


@login_required()
def getCreateThesis(request):
    form =  ThesisFrom(request.POST or None, request.FILES or None)
    postedById = adminprofile.objects.get(user = request.user.id)

    #combobox data query
    faculties = faculty.objects.all()
    department_data = department.objects.all()
    supervisor_data = supervisor.objects.all()
    thesisCategory_data = thesisCategory.objects.all()
    #table data query
    check_id = request.user.id
    adminProfile_user = get_object_or_404(adminprofile, user=check_id)
    posted_by_id = adminProfile_user.id
    thesis_data_for_table = thesis.objects.filter(posted_by = posted_by_id)

    context ={
        "form":form,
        "thesis_data_for_table":thesis_data_for_table,
        "f_data":faculties,
        "d_data":department_data,
        "s_data":supervisor_data,
        "tCategory_data":thesisCategory_data,
    }
    if request.user.is_authenticated:
        if request.method=="POST":
            facultyCombobox = request.POST.get('facultyCombobox')
            departmentCombobox = request.POST.get('departmentCombobox')
            supervisorCombobox = request.POST.get('supervisorCombobox')
            thesisCategoryCombobox = request.POST.get('projectCategoryCombobox')

            #convert combobox data as a foreginkey 
            facultyId = faculty.objects.get(id=facultyCombobox)
            departmentId = department.objects.get(id=departmentCombobox)
            supervisorId = supervisor.objects.get(id=supervisorCombobox)
            thesisCategoryId = thesisCategory.objects.get(id=thesisCategoryCombobox)
            postedById = adminprofile.objects.get(user = request.user.id)

            #get Student Information
            student_id_1 = request.POST.get('student_id_1')
            student_id_2 = request.POST.get('student_id_2')
            student_id_3 = request.POST.get('student_id_3')
            student_id_4 = request.POST.get('student_id_4')



            if form.is_valid():
                instance = form.save(commit=False)
                instance.faculty = facultyId
                instance.department = departmentId
                instance.supervisor = supervisorId
                instance.thesis_category = thesisCategoryId
                instance.posted_by = postedById
                instance.student_id_1 = student_id_1
                instance.student_id_2 = student_id_2
                instance.student_id_3 = student_id_3
                instance.student_id_4 = student_id_4
                instance.save()
                return redirect('createThesis')

    return render(request, 'addThesis.html', context)


@login_required()
def getUpdateThesis(request, id):
    postedById = adminprofile.objects.get(user = request.user.id)
    get_thesis_data = get_object_or_404(thesis, id=id)
    form =  ThesisFrom(request.POST or None, request.FILES or None, instance=get_thesis_data)
    #combobox data query
    faculties = faculty.objects.all()
    department_data = department.objects.all()
    supervisor_data = supervisor.objects.all()
    thesisCategory_data = thesisCategory.objects.all()
    context ={
        "form":form,
        "thesisData" : get_thesis_data,
        "f_data":faculties,
        "d_data":department_data,
        "s_data":supervisor_data,
        "tCategory_data":thesisCategory_data,
    }
    # print(get_project_data.supervisor)
    if request.method=="POST":
        facultyCombobox = request.POST.get('facultyCombobox')
        departmentCombobox = request.POST.get('departmentCombobox')
        supervisorCombobox = request.POST.get('supervisorCombobox')
        thesisCategoryCombobox = request.POST.get('projectCategoryCombobox')

        #get Student Information
        student_id_1 = request.POST.get('student_id_1')
        student_id_2 = request.POST.get('student_id_2')
        student_id_3 = request.POST.get('student_id_3')
        student_id_4 = request.POST.get('student_id_4')

        #convert combobox data as a foreginkey 
        facultyId = faculty.objects.get(id=facultyCombobox)
        departmentId = department.objects.get(id=departmentCombobox)
        supervisorId = supervisor.objects.get(id=supervisorCombobox)
        thesisCategoryId = thesisCategory.objects.get(id=thesisCategoryCombobox)
        postedById = adminprofile.objects.get(user = request.user.id)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.faculty = facultyId
            instance.department = departmentId
            instance.supervisor = supervisorId
            instance.thesis_category = thesisCategoryId
            instance.posted_by = postedById
            instance.student_id_1 = student_id_1
            instance.student_id_2 = student_id_2
            instance.student_id_3 = student_id_3
            instance.student_id_4 = student_id_4
            instance.save()
            return redirect('createThesis')

    return render(request, 'addThesis.html', context)


@login_required()
def getDeleteThesis(request, id):
    if request.user.is_authenticated:
        thesis_data = get_object_or_404(thesis, id=id)
        thesis_data.delete()
        return redirect('createThesis')



# Internship Form Data



@login_required()
def getCreateInternship(request):
    form =  InternshipForm(request.POST or None, request.FILES or None)
    postedById = adminprofile.objects.get(user = request.user.id)

    #combobox data query
    faculties = faculty.objects.all()
    department_data = department.objects.all()
    supervisor_data = supervisor.objects.all()
    #table data query
    check_id = request.user.id
    adminProfile_user = get_object_or_404(adminprofile, user=check_id)
    posted_by_id = adminProfile_user.id
    internship_data_for_table = internship.objects.filter(posted_by = posted_by_id)

    context ={
        "form":form,
        "internship_data_for_table":internship_data_for_table,
        "f_data":faculties,
        "d_data":department_data,
        "s_data":supervisor_data,
    }
    if request.user.is_authenticated:
        if request.method=="POST":
            facultyCombobox = request.POST.get('facultyCombobox')
            departmentCombobox = request.POST.get('departmentCombobox')
            supervisorCombobox = request.POST.get('supervisorCombobox')

            #convert combobox data as a foreginkey 
            facultyId = faculty.objects.get(id=facultyCombobox)
            departmentId = department.objects.get(id=departmentCombobox)
            supervisorId = supervisor.objects.get(id=supervisorCombobox)
            postedById = adminprofile.objects.get(user = request.user.id)

            #get Student Information
            student_id_1 = request.POST.get('student_id_1')
            student_id_2 = request.POST.get('student_id_2')
            student_id_3 = request.POST.get('student_id_3')
            student_id_4 = request.POST.get('student_id_4')



            if form.is_valid():
                instance = form.save(commit=False)
                instance.faculty = facultyId
                instance.department = departmentId
                instance.supervisor = supervisorId
                instance.posted_by = postedById
                instance.student_id_1 = student_id_1
                instance.student_id_2 = student_id_2
                instance.student_id_3 = student_id_3
                instance.student_id_4 = student_id_4
                instance.save()
                return redirect('createInternship')

    return render(request, 'addInternship.html', context)



@login_required()
def getUpdateInternship(request, id):
    postedById = adminprofile.objects.get(user = request.user.id)
    get_internship_data = get_object_or_404(internship, id=id)
    form =  InternshipForm(request.POST or None, request.FILES or None, instance=get_internship_data)
    #combobox data query
    faculties = faculty.objects.all()
    department_data = department.objects.all()
    supervisor_data = supervisor.objects.all()
    context ={
        "form":form,
        "internshipData" : get_internship_data,
        "f_data":faculties,
        "d_data":department_data,
        "s_data":supervisor_data,
    }
    # print(get_project_data.supervisor)
    if request.method=="POST":
        facultyCombobox = request.POST.get('facultyCombobox')
        departmentCombobox = request.POST.get('departmentCombobox')
        supervisorCombobox = request.POST.get('supervisorCombobox')

        #get Student Information
        student_id_1 = request.POST.get('student_id_1')
        student_id_2 = request.POST.get('student_id_2')
        student_id_3 = request.POST.get('student_id_3')
        student_id_4 = request.POST.get('student_id_4')

        #convert combobox data as a foreginkey 
        facultyId = faculty.objects.get(id=facultyCombobox)
        departmentId = department.objects.get(id=departmentCombobox)
        supervisorId = supervisor.objects.get(id=supervisorCombobox)
        postedById = adminprofile.objects.get(user = request.user.id)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.faculty = facultyId
            instance.department = departmentId
            instance.supervisor = supervisorId
            instance.posted_by = postedById
            instance.student_id_1 = student_id_1
            instance.student_id_2 = student_id_2
            instance.student_id_3 = student_id_3
            instance.student_id_4 = student_id_4
            instance.save()
            return redirect('createInternship')

    return render(request, 'addInternship.html', context)


@login_required()
def getDeleteInternship(request, id):
    if request.user.is_authenticated:
        internship_data = get_object_or_404(internship, id=id)
        internship_data.delete()
        return redirect('createInternship')


def test(request):
    return render(request, "dashboard.html")

# Index Page Graph()

def getData(request, *args, **kwargs):
   departmentData = department.objects.all()
   #For Project

   projectData = project.objects.all()
   labels = []
   listData = []
   for i in departmentData:
       labels.append(i.department_nickname)
       project_data = project.objects.filter(department_id = i.id)
       row_count=project_data.count()
       listData.append(row_count)

#  For Thesis

   thesisData = thesis.objects.all()
   labelsThesis = []
   thesisListData = []
   for j in departmentData:
       labelsThesis.append(j.department_nickname)
       thesis_data = thesis.objects.filter(department_id = j.id)
       thesis_count = thesis_data.count()
       thesisListData.append(thesis_count)
   
#    print(labelsThesis)
#    print(thesisListData)
#  For Thesis

   InternshipData = internship.objects.all()
   labelsInternship = []
   internshipListData = []
   for k in departmentData:
       labelsInternship.append(k.department_nickname)
       internship_data = internship.objects.filter(department_id = k.id)
       internship_count = internship_data.count()
       internshipListData.append(internship_count)

   #Project Category Data

    
   
    
   data = {
        "labels":labels,
        "defaultData":listData,
        "labelsThesis":labelsThesis,
        "thesisListData":thesisListData,
        "labelsInternship":labelsInternship,
        "internshipListData":internshipListData

    }

    
   
   
   return JsonResponse(data)




# Supervisor Page Graph

def getsupervisorGraphData(request, *args, **kwargs):
   supervisorData = supervisor.objects.all()
   #For Project

   projectData = project.objects.all()
   labels = []
   listData = []
   for i in supervisorData:
       labels.append(i.initial)
       project_data = project.objects.filter(supervisor_id = i.id)
       row_count=project_data.count()
       listData.append(row_count)

#  For Thesis

   thesisData = thesis.objects.all()
   labelsThesis = []
   thesisListData = []
   for j in supervisorData:
       labelsThesis.append(j.initial)
       thesis_data = thesis.objects.filter(supervisor_id = j.id)
       thesis_count = thesis_data.count()
       thesisListData.append(thesis_count)
   
#    print(labelsThesis)
#    print(thesisListData)
#  For Thesis

   InternshipData = internship.objects.all()
   labelsInternship = []
   internshipListData = []
   for k in supervisorData:
       labelsInternship.append(k.initial)
       internship_data = internship.objects.filter(supervisor_id = k.id)
       internship_count = internship_data.count()
       internshipListData.append(internship_count)

   #Project Category Data

    
   
    
   data = {
        "labels":labels,
        "defaultData":listData,
        "labelsThesis":labelsThesis,
        "thesisListData":thesisListData,
        "labelsInternship":labelsInternship,
        "internshipListData":internshipListData

    }

    
   
   
   return JsonResponse(data)


#Add QnA Form
@login_required()
def getCreateQnA(request):
    form =  QnAForm(request.POST or None, request.FILES or None)
    postedById = adminprofile.objects.get(user = request.user.id)

    
    #table data query
    check_id = request.user.id
    adminProfile_user = get_object_or_404(adminprofile, user=check_id)
    posted_by_id = adminProfile_user.id
    qnA_data_for_table = questionAndAnswer.objects.filter(posted_by = posted_by_id)

    context ={
        "form":form,
        "qnA_data_for_table":qnA_data_for_table
    }
    if request.user.is_authenticated:
        if request.method=="POST":

            #convert combobox data as a foreginkey 
            postedById = adminprofile.objects.get(user = request.user.id)



            if form.is_valid():
                instance = form.save(commit=False)
                instance.posted_by = postedById
                instance.save()
                return redirect('createQnA')

    return render(request, 'addQnA.html', context)

@login_required()
def getUpdateQnA(request, id):
    postedById = adminprofile.objects.get(user = request.user.id)
    get_QnA_data = get_object_or_404(questionAndAnswer, id=id)

    form =  QnAForm(request.POST or None, request.FILES or None, instance=get_QnA_data)
    postedById = adminprofile.objects.get(user = request.user.id)

    
    #table data query
    check_id = request.user.id
    adminProfile_user = get_object_or_404(adminprofile, user=check_id)
    posted_by_id = adminProfile_user.id
    qnA_data_for_table = questionAndAnswer.objects.filter(posted_by = posted_by_id)

    context ={
        "form":form,
        "qnA_data_for_table":qnA_data_for_table
    }
    if request.user.is_authenticated:
        if request.method=="POST":

            #convert combobox data as a foreginkey 
            postedById = adminprofile.objects.get(user = request.user.id)



            if form.is_valid():
                instance = form.save(commit=False)
                instance.posted_by = postedById
                instance.save()
                return redirect('createQnA')

    return render(request, 'addQnA.html', context)


@login_required()
def getDeleteQnA(request, id):
    if request.user.is_authenticated:
        QnA_data = get_object_or_404(questionAndAnswer, id=id)
        QnA_data.delete()
        return redirect('createQnA')