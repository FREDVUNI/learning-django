from django.urls import path
from . import views

urlpatterns =[
    path("",views.blogindex,name="blog"),
    path("<int:blogid>/details",views.blogdetails,name="blogdetails"),
    path("<category>",views.category,name="category"),
]