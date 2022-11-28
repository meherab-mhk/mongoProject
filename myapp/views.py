from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def View(request):
    obj = Employee.objects.all()
    context = {
        "data": obj
    }
    return render(request,'view.html',context)

def Add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        title = request.POST.get('title')
        salary = request.POST.get('salary')
        branch = request.POST.get('branch')

        store_data = Employee(
            name = name,
            email = email,
            title = title,
            salary = salary,
            branch = branch
        )
        print(name)
        store_data.save()
        messages.success(request,"Employe added succesfully !")
        return redirect('view')


    return render(request,'insert.html')

def Edit(request,id):
    emp = Employee.objects.get(pk=id)
    context = {
        'emp': emp
    }
    return render(request,'update.html',context)

def Update(request,id):
    emp = Employee.objects.get(pk=id)
    emp.name = request.GET['name']
    emp.email = request.GET['email']
    emp.title = request.GET['title']
    emp.salary = request.GET['salary']
    emp.branch = request.GET['branch']

    emp.save()
    messages.success(request,"Employee's information Has been Updated!")
    return redirect('view')


def Deleting(request,id):
    emp = Employee.objects.get(pk=id)
    emp.delete()
    messages.success(request,"Employee Has been deleted!")
    return redirect('view')
    