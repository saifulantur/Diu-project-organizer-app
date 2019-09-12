from django.db import models
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.

class adminprofile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.FileField(upload_to='admin/img')
	details = models.CharField(max_length=100)

	def __str__(self):
		return self.user.username

class faculty(models.Model):
	faculty_name = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.faculty_name

class department(models.Model):
	
	department_name = models.CharField(max_length=100, unique=True)
	department_nickname = models.CharField(max_length=20, unique=True)
	facultyName = models.ForeignKey(faculty, on_delete=models.CASCADE)
	posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
	

	def __str__(self):
		return self.department_name


class supervisor(models.Model):
	name = models.CharField(max_length=50)
	initial = models.CharField(max_length=10, unique=True)
	email = models.CharField(max_length=50)
	image = models.FileField(upload_to='supervisor/img')
	details = models.CharField(max_length=100)
	faculty = models.ForeignKey(faculty, on_delete=models.CASCADE)
	# department = models.ForeignKey(department, on_delete=models.CASCADE)
	department = ChainedForeignKey(
		department,
		chained_field="faculty", # the field on your own model that this field links to 
        chained_model_field="facultyName", # the field on Country that corresponds to newcontinent
        show_all=False,
        auto_choose=True,
        sort=True
	)
	posted_by = models.ForeignKey(adminprofile, on_delete=models.CASCADE)
	posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.name

class projectCategory(models.Model):
	category_project = models.CharField(max_length=50)
	department = models.ForeignKey(department, on_delete=models.CASCADE)
	posted_by = models.ForeignKey(adminprofile, on_delete=models.CASCADE)
	posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.category_project

class thesisCategory(models.Model):
	category_thesis = models.CharField(max_length=50)
	department = models.ForeignKey(department, on_delete=models.CASCADE)
	posted_by = models.ForeignKey(adminprofile, on_delete=models.CASCADE)
	posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.category_thesis



class project(models.Model):
	project_no = models.CharField(max_length=50, unique=True)
	project_title = models.CharField(max_length=100)
	project_details = models.TextField()
	project_file = models.FileField(upload_to='project/file')
	project_report = models.FileField(upload_to='project/report')
	faculty = models.ForeignKey(faculty, on_delete=models.CASCADE)
	# department = models.ForeignKey(department, on_delete=models.CASCADE)
	department = ChainedForeignKey(
		department,
		chained_field="faculty", # the field on your own model that this field links to 
        chained_model_field="facultyName", # the field on Country that corresponds to newcontinent
        show_all=False,
        auto_choose=True,
        sort=True
	)
	posted_by = models.ForeignKey(adminprofile, on_delete=models.CASCADE)
	supervisor = models.ForeignKey(supervisor, on_delete=models.CASCADE)
	# project_category = models.ForeignKey(projectCategory, on_delete=models.CASCADE)
	
	project_category = ChainedForeignKey(
		projectCategory,
		chained_field="department", # the field on your own model that this field links to 
        chained_model_field="department", # the field on Country that corresponds to newcontinent
        show_all=False,
        auto_choose=True,
        sort=True
	)
	
	#submission_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
	student_id_1 = models.CharField(max_length=50)
	student_id_2 = models.CharField(max_length=50, default=True)
	student_id_3 = models.CharField(max_length=50, default=True)
	student_id_4 = models.CharField(max_length=50, default=True)
	posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
	

	def __str__(self):
		return self.project_title

class internship(models.Model):
	internship_no = models.CharField(max_length=50, unique=True)
	internship_title = models.CharField(max_length=100)
	details = models.TextField()
	internship_report = models.FileField(upload_to='internship/report')
	faculty = models.ForeignKey(faculty, on_delete=models.CASCADE)
	# department = models.ForeignKey(department, on_delete=models.CASCADE)
	department = ChainedForeignKey(
		department,
		chained_field="faculty", # the field on your own model that this field links to 
        chained_model_field="facultyName", # the field on Country that corresponds to newcontinent
        show_all=False,
        auto_choose=True,
        sort=True
	)
	posted_by = models.ForeignKey(adminprofile, on_delete=models.CASCADE)
	supervisor = models.ForeignKey(supervisor, on_delete=models.CASCADE)
	#submission_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
	student_id_1 = models.CharField(max_length=50)
	student_id_2 = models.CharField(max_length=50, default=True)
	student_id_3 = models.CharField(max_length=50, default=True)
	student_id_4 = models.CharField(max_length=50, default=True)	
	posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.internship_title

class thesis(models.Model): 
	thesis_no = models.CharField(max_length=50, unique=True)
	thesis_title = models.CharField(max_length=100)
	details = models.TextField()
	thesis_file = models.FileField(upload_to='thesis/file')
	faculty = models.ForeignKey(faculty, on_delete=models.CASCADE)
	# department = models.ForeignKey(department, on_delete=models.CASCADE)
	department = ChainedForeignKey(
		department,
		chained_field="faculty", # the field on your own model that this field links to 
        chained_model_field="facultyName", # the field on Country that corresponds to newcontinent
        show_all=False,
        auto_choose=True,
        sort=True
	)
	posted_by = models.ForeignKey(adminprofile, on_delete=models.CASCADE)
	supervisor = models.ForeignKey(supervisor, on_delete=models.CASCADE)
	# thesis_category = models.ForeignKey(thesisCategory, on_delete=models.CASCADE)
	thesis_category = ChainedForeignKey(
		thesisCategory,
		chained_field="department", # the field on your own model that this field links to 
        chained_model_field="department", # the field on Country that corresponds to newcontinent
        show_all=False,
        auto_choose=True,
        sort=True
	)
	#submission_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
	student_id_1 = models.CharField(max_length=50)
	student_id_2 = models.CharField(max_length=50, default=True)
	student_id_3 = models.CharField(max_length=50, default=True)
	student_id_4 = models.CharField(max_length=50, default=True)
	posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.thesis_title


class questionAndAnswer(models.Model):
	question = models.CharField(max_length=100, unique=True)
	answer = models.CharField(max_length = 300)
	posted_by = models.ForeignKey(adminprofile, on_delete=models.CASCADE)

	def __str__(self):
		return self.question


