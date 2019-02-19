from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from .models import EmployeeModel

class EmployeeListView(ListView):
    model = EmployeeModel
    template_name = "index.html"
    context_object_name = "emp"


class DeleteEmployee(DeleteView):
    model = EmployeeModel
    success_url = '/emp_deleted/'

class UpdateEmployee(UpdateView):
    model = EmployeeModel
    fields = ['name','salary']
    template_name = "update.html"