from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def display(req):
    data=Student.objects.all()
    return render(req,'display_std.html',{'data':data})

def add(req):
    if req.method=='POST':
        roll=req.POST["roll_no"]
        std_name=req.POST["name"]
        std_age=req.POST["age"]
        std_email=req.POST["email"]
        std_phno=req.POST["phno"]
        data=Student.objects.create(roll_no=roll,name=std_name,age=std_age,email=std_email,phno=std_phno)
        data.save()
        return redirect(display)
    else:
        return redirect(display)
    
def edit_std(req,id):
    data=Student.objects.get(pk=id)
    if req.method=='POST':
        roll=req.POST["roll_no"]
        std_name=req.POST["name"]
        std_age=req.POST["age"]
        std_email=req.POST["email"]
        std_phno=req.POST["phno"]
        Student.objects.filter(pk=id).update(roll_no=roll,name=std_name,age=std_age,email=std_email,phno=std_phno)
        return redirect(display)
    else:
        return render(req,'edit_std.html',{'data':data})