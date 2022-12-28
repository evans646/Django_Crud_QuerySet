from django.shortcuts import render,redirect
from .models import Task
# Create your views here.
def homepage(request):
    tasks = Task.objects.all()
    return render(request,'crud/homePage.html', {'tasksLists':tasks})


def add_task(request):
            if request.method=="POST":
                title = request.POST['title']
                q = Task.objects.create(title=title)
                q.save()
                return redirect('/')
            return render(request, 'tasks/addTask.html', {})  
                     
