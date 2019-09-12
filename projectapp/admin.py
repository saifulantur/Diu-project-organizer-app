from django.contrib import admin
from.models import adminprofile,department, supervisor, projectCategory, thesisCategory, project, internship, thesis, faculty, questionAndAnswer


# Register your models here.

class facultyModel(admin.ModelAdmin):
    search_fields = ('faculty_name',)
    
    class Meta:
        Model = faculty

admin.site.register(faculty, facultyModel)

class departmentModel(admin.ModelAdmin):
    list_display = ["__str__", "posted_on"]
    search_fields = ('department_name', 'department_nickname', )
    list_per_page = 10
    list_filter = ["posted_on", "department_name"]

    class Meta:
        Model = department

admin.site.register(department, departmentModel)

class ProjectModel(admin.ModelAdmin):
    list_display = ["__str__", "project_no","department","project_category","posted_by","posted_on"]
    search_fields = ('project_no', 'project_title',"department","posted_by","posted_on")
    list_per_page = 10
    list_filter = ["project_no", "project_title","department","posted_by","posted_on"]

    class Meta:
        Model = project 

admin.site.register(project, ProjectModel)

class SupervisorModel(admin.ModelAdmin):
    list_display = ["__str__", "department","initial","posted_by","posted_on"]
    search_fields = ('name', 'initial', 'department',"posted_by","posted_on" )
    list_per_page = 10
    list_filter = ["name", "department","posted_by","posted_on"]

    class Meta:
        Model = supervisor
admin.site.register(supervisor, SupervisorModel)

class ProjectCategoryModel(admin.ModelAdmin):
    list_display = ["__str__", "department","posted_by","posted_on"]
    search_fields = ('name', 'category_project', 'department',"posted_on" )
    list_per_page = 10
    list_filter = ["category_project", "department","posted_on"]

    class Meta:
        Model = projectCategory
admin.site.register(projectCategory, ProjectCategoryModel)

class ThesisCategoryModel(admin.ModelAdmin):
    list_display = ["__str__", "department","posted_by","posted_on"]
    search_fields = ('name', 'category_thesis', 'department',"posted_on" )
    list_per_page = 10
    list_filter = ["category_thesis", "department","posted_on"]

    class Meta:
        Model = thesisCategory
admin.site.register(thesisCategory, ThesisCategoryModel)

class InternshipModel(admin.ModelAdmin):
    list_display = ["__str__", "internship_no","department","posted_by","posted_on"]
    search_fields = ('internship_title', 'internship_no', 'department',"posted_by","posted_on" )
    list_per_page = 10
    list_filter = ["internship_title", "internship_no","department","posted_by","posted_on"]

    class Meta:
        Model = internship
admin.site.register(internship, InternshipModel)

class ThesisModel(admin.ModelAdmin):
    list_display = ["__str__", "thesis_no","department","thesis_category","posted_by","posted_on"]
    search_fields = ('thesis_no', 'thesis_title',"department","thesis_category","posted_by","posted_on")
    list_per_page = 10
    list_filter = ["thesis_no", "thesis_title","department","thesis_category","posted_by","posted_on"]

    class Meta:
        Model = thesis 
admin.site.register(thesis, ThesisModel)

admin.site.register(adminprofile)
admin.site.register(questionAndAnswer)