from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
std=[]
def add(request):
    if request.method=='POST':
        roll=request.POST['roll']
        name=request.POST['name']
        age=request.POST['age']
        mark=request.POST['mark']
        std.append({'name':roll,'name':name,'age':age,'mark':mark})
        print(std)
        return redirect(add)
    return render(request,'index.html',{'add':std})