from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator
from .form import TaskForm
from .models import Task


 # Create your views here.
def homepage(request):
    new_tasks = Task.objects.all()
    return render(request,'crud/homePage.html', {'tasks':new_tasks})


def add_task(request):
            if request.method=="POST":
                name = request.POST['name']
                description = request.POST['description']
                task = Task.objects.create(name=name,description=description)
                task.save()
                return redirect('/')
            return redirect('/') 
                     
def all_tasks_list(request):
    task_lists = Task.objects.all()
    paginator = Paginator(task_lists,4)
    page = request.GET.get('page')
    all_tasks = paginator.get_page(page)
    return render(request, 'tasks/allTasksPage.html', {'all_tasks':all_tasks})
                              
                           
def view_task(request,pk):
      task_detail = get_object_or_404(Task, pk=pk) 
      return render(request, 'tasks/detail.html', {'task':task_detail})                       
                         
def update_task(request, pk):
            selected_task = Task.objects.get(pk=pk)
            form = TaskForm(instance=selected_task)
            if request.method=="POST":
                filled_form = TaskForm(request.POST, instance=selected_task)
                if filled_form.is_valid():
                    filled_form.save()
                    form = filled_form
                    return redirect('/')
            return render(request, 'tasks/updateTask.html', {'taskform':form, 'task':selected_task})     
        
def search_everything(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        search_results = Task.objects.filter(name__contains=searched)
        return render(request, 'interface/searchResults.html',{'searched':searched,'searched_results':search_results})
    else:
        return redirect('/')      
             
             
def delete_task(request, pk):
            task = Task.objects.get(pk=pk)
            task.delete()
            return redirect('/')   
                                      