from django.views.generic import ListView
from django.shortcuts import render
from .models import Student

class ViewAllStudents(ListView):

   # Example to View All Rows and Colums
   # model = Student
   # template_name = "student_details.html"

   model = Student
   queryset = Student.objects.values('idno','name','grade','clas')
   template_name = "student_details.html"

