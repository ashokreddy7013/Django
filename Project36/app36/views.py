from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DeleteView

from .models import EmployeeReg

class EmployeeRegFormView(CreateView):
    model = EmployeeReg
    fields = ["name","age","contact","email","password"]
    template_name = "index.html"

class EmployeeDelete(DeleteView):
    model = EmployeeReg