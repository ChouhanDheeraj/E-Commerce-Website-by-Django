
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="Shop home"),
    path("blogpost/<int:id>",views.blogpost,name="blogPost"),
]
