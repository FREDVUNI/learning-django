from django.shortcuts import render,get_object_or_404,redirect
from . forms import TaskForm
from django.contrib import messages
from . models import Task
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,('Item has been saved.'))
        return redirect("list")
    else:
        form = TaskForm()
        items = Task.objects.all()
        context = {'items':items,"form":form}
        return render(request,"tasks/list.html",context)

def update(request,pk):
    if request.method == 'POST':
        task = Task.objects.get(id=pk)
        form = TaskForm(request.POST or None , instance = task)
        
        if form.is_valid():
            form.save()
            messages.success(request,('Item has been updated.'))
            return redirect('list')
    else:
        form = Task.objects.get(id=pk)
        context ={'form':form}
        return render(request,"tasks/edit.html",context)

def delete(request,pk):        
    task =Task.objects.get(id=pk)
    task.delete()
    messages.success(request,('Item has been deleted.'))
    return redirect("list")