from django.shortcuts import render,redirect
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
                     
                           
# def update(request, id):
#             selected_task = Todo.objects.get(id=id)
#             if request.method=="POST":
#                 form = TodoForm(request.POST, instance=selected_task)
#                 if form.is_valid():
#                     form.save()
#                     return redirect('/tasks/')
#             else:
#                 form = TodoForm(instance=selected_task)
#             return render(request, 'update_task.html', {'form':form})
                                      
# def delete(request, id):
#             task = Todo.objects.get(id=id)
#             task.delete()
#             return redirect('/tasks/')   
                                      