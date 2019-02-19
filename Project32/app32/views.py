from django.shortcuts import render
from django.views.generic import DetailView
from .models import Studnet

class StudentDetails(DetailView):
    model = Studnet
    template_name = "app32/Studnet_details.html"
