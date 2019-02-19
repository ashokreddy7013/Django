from django.shortcuts import render
from django.views.generic import View
from .models import Contacts
from django.core.paginator import Paginator


class MyContacts(View):
    def get(self,request):
        res = Contacts.objects.all()
        p = Paginator(res,3)
        number = request.GET.get("no")
        p1 = p.get_page(number)
        return render(request,"index.html",{"p":p1})

