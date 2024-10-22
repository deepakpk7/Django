from django.shortcuts import render,redirect
from django.http import HttpResponse


# Create your views here.
def fun1(request):
    return HttpResponse("Function 1")

def fun2(request):
    a={'name':'dpk','age':20}
    return HttpResponse(a)
def fun3(request,a,b):
    return HttpResponse(a)

def fun4(request,a,b,c):
    if a>b and a>c:
        return HttpResponse(a)
    elif b>a and b>c:
        return HttpResponse(b)
    else :
        return HttpResponse(c)
    
    

    
def index_page(req):
    name="Deepak"
    age=20
    place="Calicut"
    return render(req,'index.html',{'name':name,'age':age,'place':place})

def demo(req):
    # l=[1,2,3,4,5,6,7,8,9,10,]
    l=[{'name':'deepak','age':20},{'name':'ibin','age':21},{'name':'alen','age':21}]
    d={'name':'Deepak','age':20}
    return render(req,'demo.html',{"data":l,"data2":d})

def second(req):
    return render(req,'second.html')

todo=[{'id':'1','task':'task1'},{'id':'2','task':'task2'}]
def todo1(request):
    if request.method=='POST':
        id=request.POST['id']
        task=request.POST['task']
        todo.append({'id':id,'task':task})
        print(todo)
        return redirect(todo1)
    return render(request,'todo.html',{'todo1':todo})

def edit_form(req,id):
    task=''
    for i in todo:
        if i['id']==id:
            task=i
    if req.method=='POST':
        id=req.POST['id']
        task1=req.POST['task']
        task['id']=id
        task['task']=task1
        print(todo)
        return redirect(todo1)
    return render(req,'edit.html',{'task':task})

def delete_fun(req,id):
    for i in todo:
        if i['id']==id:
            todo.remove(i)
    return redirect(todo1)  
    
