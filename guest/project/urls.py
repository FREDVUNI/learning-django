from django.urls import path
from . import views

urlpatterns =[
    path("",views.IndexView.as_view(),name="index"),
    path("company/create",views.createCompany.as_view(),name="company"),
    path("<str:slug>",views.companyDetails.as_view(),name="details"),
    path("<str:slug>/update",views.companyUpdate.as_view(),name="edit"),
    path("<str:slug>/delete",views.companyDelete.as_view(),name="delete"),
    path("search/company",views.search,name="search"),

    path("languages/available",views.languages.as_view(),name="languages"),
    path("languages/create",views.createLang.as_view(),name="language"),
    path("language/<str:slug>/edit",views.UpdateLang.as_view(),name="editLang"),
    path("language/<str:slug>/delete",views.deleteLang.as_view(),name="deleteLang"),

    path("programmers/available",views.programmer.as_view(),name="programmers"),
    path("programmers/create",views.add.as_view(),name="add")
]