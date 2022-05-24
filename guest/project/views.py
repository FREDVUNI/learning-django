from django.shortcuts import render
from django.views import generic
from .models import Company,Language,Programmer
from django.urls import reverse_lazy
from django.db.models import Q

# Create your views here.
class IndexView(generic.ListView):
    template_name ="project/index.html"
    context_object_name ="company"

    def get_queryset(self):
        return Company.objects.all()        

class createCompany(generic.CreateView):
    model = Company
    fields =["name","location","image","slug"]

class companyDetails(generic.DetailView):
    model = Company
    context_object_name ="companys"
    template_name ="project/details.html"

class companyUpdate(generic.UpdateView):
    model = Company
    fields =["name","location","image","slug"]

class companyDelete(generic.DeleteView):
    model = Company
    success_url = reverse_lazy("index")    

def search(request):
    q = request.GET.get('search' or None)

    if q is not None:
        search = Company.objects.filter(Q(name__contains = q)| Q(location__contains = q))
        context ={"company":search,"q":q}
        return render(request,"project/search.html",context)

class languages(generic.ListView):
    template_name ="project/languages.html"
    context_object_name ="lang"

    def get_queryset(self):
        return Language.objects.all()        

class createLang(generic.CreateView):
    model = Language
    fields =["name"]    

class UpdateLang(generic.UpdateView):
    model = Language
    fields =["name"]          

class deleteLang(generic.DeleteView):
    model = Language
    success_url= reverse_lazy("languages")

class programmer(generic.ListView):
    template_name ="programmers.html"
    context_object_name="programmers"

    def get_queryset(self):
        return Programmer.objects.all()   

class add(generic.CreateView):
    model = Programmer
    fields ='__all__'       