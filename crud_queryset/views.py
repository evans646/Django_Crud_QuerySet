from django.shortcuts import render,redirect
from .form import TaskForm
from .models import Task
# Create your views here.


def homepage(request):
    tasks = Task.objects.all()
    return render(request,'crud/homePage.html', {'taskLists':tasks})


def add_task(request):
            if request.method=="POST":
                name = request.POST['name']
                description = request.POST['description']
                task = Task.objects.create(name=name,description=description)
                task.save()
                return redirect('/')
            return redirect('/') 
                     
                           
def update_task(request, pk):
            selected_task = Task.objects.get(pk=pk)
            form = TaskForm(instance=selected_task)
            if request.method=="POST":
                filled_form = TaskForm(request.POST, instance=selected_task)
                if filled_form.is_valid():
                    filled_form.save()
                    form = filled_form
                    note = 'Your order has been processed.'
                    return render(request, 'task/editTask.html', {'taskform':form, 'task':selected_task, 'note':note})
            return render(request, 'task/editTask.html', {'taskform':form, 'task':selected_task})     
        
        
             
# def delete(request, id):
#             task = Todo.objects.get(id=id)
#             task.delete()
#             return redirect('/tasks/')   
                                      