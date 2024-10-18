from django.shortcuts import render
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