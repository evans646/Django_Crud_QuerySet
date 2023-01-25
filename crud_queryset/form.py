from django import forms
from .models import  Task

class TaskForm(forms.ModelForm):
    
    class Meta:
            model = Task
            fields = ['name', 'description'] #input fields 
            labels = {
            "name": "Name",
            "description": "Description",
            }
            attrs={'class':'form-control'} #adding custom classes to forms
