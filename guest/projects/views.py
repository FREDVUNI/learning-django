from django.shortcuts import render
from . models import Project
# Create your views here.
def index(request):
    projects = Project.objects.all()
    template_name = "projects/index.html"
    context ={"projects" : projects}
    return render(request,template_name,context)

def details(request,id):
    project = Project.objects.get(pk=id)
    template_name = "projects/details.html"
    context ={"project" : project}
    return render(request,template_name,context)    