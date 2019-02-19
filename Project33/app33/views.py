from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView
from .models import Employee

class MyEmpDetails(ListView):
    context_object_name = "sathya"
    model = Employee
    queryset = Employee.objects.values('id')
    template_name = "view_all_employees.html"

class EmpDetails(DetailView):
    context_object_name = "tech"
    model = Employee
    template_name = "view_employee.html"