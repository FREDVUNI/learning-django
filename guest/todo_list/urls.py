from django .urls import path
from . import views

urlpatterns =[
    path("",views.home,name="index"),
    path("<int:todo_id>/delete",views.delete,name="delete"),
    path("<int:todo_id>/edit",views.edit,name="edit"),
    path("<int:todo_id>/crossoff",views.crossoff,name="crossoff"),
    path("<int:todo_id>/uncross",views.uncross,name="uncross"),
]