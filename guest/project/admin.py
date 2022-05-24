from django.contrib import admin
from . models import Company,Language,Programmer

# Register your models here.
admin.site.register(Company)
admin.site.register(Language)
admin.site.register(Programmer)