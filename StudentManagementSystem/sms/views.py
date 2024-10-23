from django.shortcuts import render
from .models import *
# Create your views here.
def display(req):
    data=Student.objects.all()
    return render(req,'display_std.html',{'data':data})
   