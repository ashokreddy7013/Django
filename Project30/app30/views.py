from django.shortcuts import render
from django.views.generic import View
from django.views.generic import ListView
from .models import Employee

class SaveDetails(View):
    def post(self,request):
        idno = request.POST.get("t1")
        name = request.POST.get("t2")
        salary = request.POST.get("t3")
        designation = request.POST.get("t4")

        emp = Employee(designation=designation,name=name,salary=salary,idno=idno)
        emp.save()
        return render(request,"index.html",{"message":"Data Saved"})

class ViewAllEmployees(ListView):
    model = Employee