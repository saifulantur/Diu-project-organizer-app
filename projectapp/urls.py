from django.urls import path
from.import views
from .views import getData
# from .views import get_data



urlpatterns = [
    #Dashboard/Index page routing
    
    path('', views.index, name="index"),
    
    path('allproject/', views.getallproject, name="allproject"),
    path('allthesis/', views.getallthesis, name="allthesis"),
    path('allinternship/', views.getallinternship, name="allinternship"),
    path('allfaculty/', views.getallfaculty, name="allfaculty"),

    path('project-query/<int:id>', views.getqueryprojects, name="queryproject"),
    path('thesis-query/<int:id>', views.getquerythesis, name="querythesis"),

    path('project-query-list/<int:id>', views.getqueryprojectslist, name="queryprojectlist"),
    path('thesis-query-list/<int:id>', views.getquerythesislist, name="querythesislist"),
    path('internship-query-list/<int:id>', views.getqueryinternshiplist, name="queryinternshiplist"),

    path('supervisors/', views.supervisors, name="supervisors"),

    path('login/', views.getLogin, name="login"),
    path('logout/', views.getLogout, name="logout"),

    path('test/', views.test, name="test"),
    #Index Graph
    path('getData/', views.getData, name="getData"),
    #Category Graph
    path('getProjectCategoryData/', views.getProjectCategoryData, name="getProjectCategoryData"),
    path('getThesisCategoryData/', views.getThesisCategoryData, name="getThesisCategoryData"),
    #Supervisor Form Graph
    path('supervisorGraphData/', views.getsupervisorGraphData, name="getsupervisorGraphData"),
    #Others
    path('QnA/', views.getQuestion, name="question"),
    path('PageNotFound/', views.PageNotFound, name="PageNotFound"),

    #Project Form Data

    path('create/', views.getCreate, name="create"),
    path('update/<int:id>', views.getUpdate, name="update"),
    path('delete/<int:id>', views.getDelete, name="delete"),

    #Supervisor Form Data

    path('createSupervisor/', views.getCreateSupervisor, name="createSupervisor"),
    path('updateSupervisor/<int:id>', views.getUpdateSupervisor, name="updateSupervisor"),
    path('deleteSupervisor/<int:id>', views.getDeleteSupervisor, name="deleteSupervisor"),

    #Project Category Form Data

    path('createProjectCategory/', views.getCreateProjectCategory, name="createProjectCategory"),
    path('updateProjectCategory/<int:id>', views.getUpdateProjectCategory, name="updateProjectCategory"),
    path('deleteProjectCategory/<int:id>', views.getDeleteProjectCategory, name="deleteProjectCategory"),

    #Thesis Category Form Data

    path('createThesisCategory/', views.getCreateThesisCategory, name="createThesisCategory"),
    path('updateThesisCategory/<int:id>', views.getUpdateThesisCategory, name="updateThesisCategory"),
    path('deleteThesisCategory/<int:id>', views.getDeleteThesisCategory, name="deleteThesisCategory"),

    #Thesis Form Data

    path('createThesis/', views.getCreateThesis, name="createThesis"),
    path('updateThesis/<int:id>', views.getUpdateThesis, name="updateThesis"),
    path('deleteThesis/<int:id>', views.getDeleteThesis, name="deleteThesis"),

    
    #Internship Form Data

    path('createInternship/', views.getCreateInternship, name="createInternship"),
    path('updateInternship/<int:id>', views.getUpdateInternship, name="updateInternship"),
    path('deleteInternship/<int:id>', views.getDeleteInternship, name="deleteInternship"),

    
    #Add Question And Answer Form

	path('CreateQnA/', views.getCreateQnA, name="createQnA"),
    path('UpdateQnA/<int:id>', views.getUpdateQnA, name="UpdateQnA"),
    path('DeleteQnA/<int:id>', views.getDeleteQnA, name="DeleteQnA"),
  
]

