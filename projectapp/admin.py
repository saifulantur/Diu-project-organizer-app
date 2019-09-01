from django.contrib import admin
from.models import department, supervisor, projectCategory, thesisCategory, project, internship, thesis, student, faculty


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

admin.site.register(supervisor)
admin.site.register(projectCategory)
admin.site.register(thesisCategory)
admin.site.register(project)
admin.site.register(internship)
admin.site.register(thesis)
admin.site.register(student)