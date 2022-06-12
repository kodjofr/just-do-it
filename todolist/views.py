from django.shortcuts import redirect, render
from todolist.forms import TaskForm

from todolist.models import Task


def index(request):
    
    form = TaskForm()
    
    # check if HTTP method 
    if request.method == "POST":
        # instanciate form with data
        form = TaskForm(request.POST)
        
        # check form validity
        if form.is_valid():
            
            #save data
            form.save()
            #redirect url to index
            return redirect("index")
    
    tasks = Task.objects.all()
    return render(request,  "index.html", 
                            {"tasks": tasks,
                            "task_form":form},)

def update(request):
    return render(request,"update.html")

def delete(request):
    return render(request,"delete.html")