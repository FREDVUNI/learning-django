#views.py
from . forms import ListForm
from . models import List
from django . shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django .views import generic
from django .views import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        items = List.objects.all()

        if form.is_valid():
            form.save()
            context ={'items':items}
            messages.success(request,('Item has been added.))
            return render(request,'todo/home.html',context)
    else:
        items = List.objects.all()
        context ={'items':items}
        return render(request,'todo/home.html',context)

def create(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ListForm()
        context ={'form':form}
        return render(request,'todo/home.html',context)

class index(generic.ListView):
    context_object_name = "items"
    template_name ="todo/home.html"

    def get_queryset(self):
        return List.objects.all
class create(generic.CreateView):
    model = List
    fields =['item','completed']

class details(generic.DetailView):
    model = List
    template_name ="todo/deatails.html" 

class delete(generic.DeleteView):
    model =List
    success_url = reverse_lazy("home")                   

class edit(generic.UpdateView):
    model =List
    fields =['item','completed']

def delete(request,id):
    item = get_object_or_404(List,pk=id)        
    item = List.objects.get(pk=id)

    item.delete()
    mrssages.success(request,('Item has been deleted))
    return redirect("home)

def crossoff(request,id):
    item = get_object_or_404(List,pk=id)        
    item = List.objects.get(pk=id)

    item.completed = True
    item.save()
    return redirect('home)  

def uncross(request,id):
    item = get_object_or_404(List,pk=id)        
    item = List.objects.get(pk=id)

    item.completed = False
    item.save()
    return redirect('home) 

def edit(request,id)
    if request.method == 'POST':
        item = List.objects.get(pk=id)
        form = ListForm(request.POST or None,instance=item)
        if form.is_valid()
            form.save()

            context={"item":item}
            messages.success(request,('Item has been editted.))
            return render(request,'todo/edit.html',context)

    else:
        item = List.objects.get(pk=id)
        context={"item":item}
        return render(request,'todo/edit.html',context)

def search(request):
    if request.method == 'GET':
        search = request.GET.get('query')
        if search is not None:
            searched = List.objects.filter(item__iexact = search)
            context ={'searched':searched}
            return render(request,'todo/search.html',context)


"""This is about the media"""
""" settings.py """
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL ="/media/"

""" urls.py in the project """

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root = STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root = MEDIA_ROOT)

