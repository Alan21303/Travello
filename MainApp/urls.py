from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("about",views.about,name="about"),
    path("news",views.news,name="news"),
    path("contact",views.contact,name="contact"),
    path("index",views.home,name="index"),
    path("admins",views.admins,name="admins"),
    path("Admin_edit",views.Admin_edit,name="Admin_edit"),
    path("Admin_add",views.Admin_add,name="Admin_add"),
    path("Admin_view",views.Admin_view,name="Admin_view"),

    
]