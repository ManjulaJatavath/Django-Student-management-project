from django.urls import path
from. views import*
urlpatterns = [
  
    path("",home,name="home"),
    #path("home/",home),
    #path("home/"),
    path("add/",add),
    path("delete/<int:roll>",delete),
    path("update/<int:roll>",update),
    path("do_update/<int:roll>",do_update),
]