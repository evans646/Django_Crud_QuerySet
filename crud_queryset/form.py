from django import forms
from .models import  Task

class TaskForm(forms.ModelForm):

    class Meta:
            model = Task
            fields = ['name', 'description']
            labels = {
            "name": "Name",
            "description": "Description",
            }
            attrs={'class':'form-control'}
            

    def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)
           self.fields['name'].widget.attrs.update({'class': 'form-control'})
           self.fields['description'].widget.attrs.update({'class':'form-control'})