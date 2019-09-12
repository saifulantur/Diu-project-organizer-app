from django import forms  
from .models import project, supervisor, projectCategory, thesisCategory, thesis, internship, questionAndAnswer
from django.forms import TextInput, Textarea, FileInput, Select

#Project Form
class ProjectForm(forms.ModelForm):  
    class Meta:  
        model = project  
        
        fields = [
            'project_no',
            'project_title',
            'project_details',
            'project_file',
            'project_report'
            ]  
        widgets = {
            'project_no': TextInput(attrs={'placeholder': 'Enter Project No'}),
            'project_title': TextInput(attrs={'placeholder': 'Enter Project Title'}),
            'project_details': Textarea(attrs={'placeholder': 'Enter Project Details'})
        }

#Supervisor Form

class SupervisorForm(forms.ModelForm):
    class Meta:
        model = supervisor

        fields = [
            'name',
            'initial',
            'email',
            'image',
            'details'
        ]
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Enter Supervisor Name'}),
            'initial': TextInput(attrs={'placeholder': 'Enter Supervisor Initial'}),
            'email': TextInput(attrs={'placeholder': 'Enter Supervisor Email'}),
            'details': Textarea(attrs={'placeholder':'Example: http://faculty.daffodilvarsity.edu.bd/profile/cse/Fahmida-Afrin.html', 'rows':3}),
        }

#Project Category

class ProjectCategoryForm(forms.ModelForm):
    class Meta:
        model = projectCategory

        fields = [
            'category_project'
        ]
        widgets = {
            'category_project': TextInput(attrs={'placeholder': 'Enter Project Category Name'})
        
        }
        
#Thesis Category

class ThesisCategoryForm(forms.ModelForm):
    class Meta:
        model = thesisCategory

        fields = [
            'category_thesis'
        ]
        widgets = {
            'category_thesis': TextInput(attrs={'placeholder': 'Enter Thesis Category Name'})
        
        }

#Add Thesis

class ThesisFrom(forms.ModelForm):  
    class Meta:  
        model = thesis  
        
        fields = [
            'thesis_no',
            'thesis_title',
            'details',
            'thesis_file'
            ]  
        widgets = {
            'thesis_no': TextInput(attrs={'placeholder': 'Enter Thesis No'}),
            'thesis_title': TextInput(attrs={'placeholder': 'Enter Thesis Title'}),
            'details': Textarea(attrs={'placeholder': 'Enter Thesis Details'})
        }

#Add Internship

class InternshipForm(forms.ModelForm):  
    class Meta:  
        model = internship  
        
        fields = [
            'internship_no',
            'internship_title',
            'details',
            'internship_report'
            ]  
        widgets = {
            'internship_no': TextInput(attrs={'placeholder': 'Enter Internship No'}),
            'internship_title': TextInput(attrs={'placeholder': 'Enter Internship Title'}),
            'details': Textarea(attrs={'placeholder': 'Enter Internship Details'})
        }


#Add QuestionAndAnswer

class QnAForm(forms.ModelForm):  
    class Meta:  
        model = questionAndAnswer  
        
        fields = [
            'question',
            'answer',
            ]  
        widgets = {
            'question': TextInput(attrs={'placeholder': 'Enter question'}),
            'answer': Textarea(attrs={'placeholder': 'Enter answer'})
        }