from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm
# Create your views here.

def home_view(request):
    emp=Employee.objects.all()
    print(type(emp))
    return render(request,'empdetails/home.html',{'emp':emp})

def insert_view(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'empdetails/insert.html',{'form':form})

def delete_view(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return redirect('/')


def update_view(request,id):
    emp=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=emp)
        form.save()
        return redirect('/')

    return render(request,'empdetails/update.html',{'emp':emp})

