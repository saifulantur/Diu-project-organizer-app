from django.db import models


# Create your models here.
class faculty(models.Model):
	#id = models.AutoField(primary_key=True)
	faculty_name = models.CharField(max_length=100)
	def __str__(self):
		return self.faculty_name

class department(models.Model):
	
	department_name = models.CharField(max_length=100)
	department_nickname = models.CharField(max_length=20)
	facultyName = models.ForeignKey(faculty, on_delete=models.CASCADE)
	posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
	

	def __str__(self):
		return self.department_name


class supervisor(models.Model):
	name = models.CharField(max_length=50)
	initial = models.CharField(max_length=10)
	email = models.CharField(max_length=50)
	image = models.FileField(upload_to='supervisor/img')
	details = models.CharField(max_length=100)
	facultyName = models.ForeignKey(faculty, on_delete=models.CASCADE)
	department = models.ForeignKey(department, on_delete=models.CASCADE)
	posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.name

class projectCategory(models.Model):
	category_project = models.CharField(max_length=50)
	department = models.ForeignKey(department, on_delete=models.CASCADE)
	posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.category_project

class thesisCategory(models.Model):
	category_thesis = models.CharField(max_length=50)
	department = models.ForeignKey(department, on_delete=models.CASCADE)
	posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.category_thesis



class project(models.Model):
	project_no = models.CharField(max_length=50)
	project_title = models.CharField(max_length=100)
	project_details = models.TextField()
	project_file = models.FileField(upload_to='project/file')
	project_report = models.FileField(upload_to='project/report')
	faculty = models.ForeignKey(faculty, on_delete=models.CASCADE)
	department = models.ForeignKey(department, on_delete=models.CASCADE)
	supervisor = models.ForeignKey(supervisor, on_delete=models.CASCADE)
	project_category = models.ForeignKey(projectCategory, on_delete=models.CASCADE)
	submission_date = models.DateField(auto_now=False, auto_now_add=False)
	posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
	

	def __str__(self):
		return self.project_title

class internship(models.Model):
	internship_no = models.CharField(max_length=50)
	industry_name = models.CharField(max_length=100)
	details = models.TextField()
	internship_report = models.FileField(upload_to='internship/report')
	faculty = models.ForeignKey(faculty, on_delete=models.CASCADE)
	department = models.ForeignKey(department, on_delete=models.CASCADE)
	supervisor = models.ForeignKey(supervisor, on_delete=models.CASCADE)
	posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.industry_name

class thesis(models.Model):
	thesis_no = models.CharField(max_length=50)
	name = models.CharField(max_length=100)
	details = models.TextField()
	thesis_file = models.FileField(upload_to='thesis/file')
	faculty = models.ForeignKey(faculty, on_delete=models.CASCADE)
	department = models.ForeignKey(department, on_delete=models.CASCADE)
	supervisor = models.ForeignKey(supervisor, on_delete=models.CASCADE)
	thesis_category = models.ForeignKey(thesisCategory, on_delete=models.CASCADE)
	posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.name



class student(models.Model):
	student_id = models.CharField(max_length=50)
	student_name = models.CharField(max_length=50)
	student_email = models.CharField(max_length=50)
	project = models.ForeignKey(project, on_delete=models.CASCADE)
	thesis = models.ForeignKey(thesis, on_delete=models.CASCADE)
	internship = models.ForeignKey(internship, on_delete=models.CASCADE)
	supervisor = models.ForeignKey(supervisor, on_delete=models.CASCADE)
	posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.student_name

