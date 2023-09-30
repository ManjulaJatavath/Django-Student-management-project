from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Student

# Create your views here.
def home(request):
    std=Student.objects.all()

    return render(request,"home.html",{'std':std})

def add(request):
    if request.method=='POST':
        print("Added")
        # retrive the user input
        stds_roll=request.POST.get("std_roll")
        stds_name=request.POST.get("std_name")
        stds_email=request.POST.get("std_email")
        stds_address=request.POST.get("std_address")
        stds_phone=request.POST.get("std_phone")

        #create an object for models
        s=Student()
        s.roll=stds_roll
        s.name=stds_name
        s.email=stds_email
        s.address=stds_address
        s.phone=stds_phone

        s.save()
        return redirect("/std/home/")
    
    

    return render(request,"add.html",{})
def delete(request,roll):
    s=Student.objects.get(pk=roll)
    s.delete()

    return redirect("/std/home/")

def update(request,roll):
    std=Student.objects.get(pk=roll)

    return render(request,"update.html",{'std':std})
    
   



def do_update(request,roll):
    std_roll=request.POST.get("std_roll")
    std_name=request.POST.get("std_name")
    std_email=request.POST.get("std_email")
    std_address=request.POST.get("std_address")
    std_phone=request.POST.get("std_phone")

    std=Student.objects.get(pk=roll)

    std.roll=std_roll
    std.name=std_name
    std.email=std_email
    std.address=std_address
    std.phone=std_phone

    std.save()
    return redirect("/std/home/")