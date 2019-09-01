from django.urls import path
from.import views
# from .views import get_data



urlpatterns = [
    path('', views.index, name="index"),
    path('allproject/', views.getallproject, name="allproject"),
    path('allthesis/', views.getallthesis, name="allthesis"),
    path('allinternship/', views.getallinternship, name="allinternship"),
    path('allfaculty/', views.getallfaculty, name="allfaculty"),
    path('project-query/<int:id>', views.getqueryprojects, name="queryproject"),
    path('project-query-list/<int:id>', views.getqueryprojectslist, name="queryprojectlist"),
    path('thesis-query/<int:id>', views.getquerythesis, name="querythesis"),
    path('thesis-query-list/<int:id>', views.getquerythesislist, name="querythesislist"),
    path('internship-query-list/<int:id>', views.getqueryinternshiplist, name="queryinternshiplist"),
    path('supervisors/', views.supervisors, name="supervisors"),
    path('login/', views.getLogin, name="login"),
    path('logout/', views.getLogout, name="logout"),

    # path('api/data', views.get_data, name="api-data"),

    path('test/', views.test, name="test"),
    path('PageNotFound/', views.PageNotFound, name="PageNotFound"),

    #Form Data

    path('add-projects', views.addProjectData, name="addProjectData"),
	
  
]

