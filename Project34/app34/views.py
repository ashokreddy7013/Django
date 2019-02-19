

from django.views.generic import FormView
from .forms import MyRegisterForm


class Register(FormView):
    form_class = MyRegisterForm
    template_name = "index.html"
