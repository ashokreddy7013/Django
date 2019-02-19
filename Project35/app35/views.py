from django.shortcuts import render
from .forms import Registration
from django.views.generic import FormView


class NewRegistration(FormView):
    form_class = Registration
    template_name = "index.html"
