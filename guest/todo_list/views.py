from django .shortcuts import render,redirect
from .forms import ListForm
from . models import List
from django.contrib import messages

def home(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all
            context ={"all_items":all_items}
            messages.success(request,('Item has been added.'))
            return render(request,"todo_list/home.html",context)
    else:        
        all_items = List.objects.all
        context ={"all_items":all_items}
        return render(request,"todo_list/home.html",context)

def delete(request,todo_id):
    item = List.objects.get(pk=todo_id)
    item.delete()
    messages.success(request,("Item has been deleted."))
    return redirect('index')

def crossoff(request,todo_id):
    item =  List.objects.get(pk=todo_id)
    item.completed = True
    item.save()
    return redirect('index')

def uncross(request,todo_id):
    item =  List.objects.get(pk=todo_id)
    item.completed = False
    item.save()
    return redirect('index')

def edit(request,todo_id):
    if request.method == 'POST':
        item = List.objects.get(pk=todo_id)
        form = ListForm(request.POST or None , instance = item)
        
        if form.is_valid():
            form.save()
            messages.success(request,('Item has been updated.'))
            return redirect('index')
    else:
        item = List.objects.get(pk=todo_id)
        context ={'item':item}
        return render(request,"todo_list/edit.html",context)