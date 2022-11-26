from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    obj = Employee.objects.all()
    context = {
        "data": obj
    }
    return render(request,'index.html',context)