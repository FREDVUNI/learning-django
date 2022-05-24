from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name="list"),
    path('<int:pk>',views.update,name="update"),
    path('<int:pk>/delete',views.delete,name="delete"),
]