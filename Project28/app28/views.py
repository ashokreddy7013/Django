from django.shortcuts import render
from django.shortcuts import redirect

from django.views.generic import View

class IndexView(View):
    def get(self, request):
        request.session["status"] = False
        return render(request, "inde.html")

class ViewProduct(View):
    def get(self,request):
        return render(request,"products.html")



def payment(request):
    list_items = request.POST.getlist("p1")
    if list_items == []:
        return render(request,"products.html",{"error":"Please Select One or More Item's"})
    else:
        status = request.session["status"]
        if status:
            return render(request,"payment.html")
        else:
            return redirect("/login/")


def logincheck(request):
    uname = request.POST.get("uname")
    upass = request.POST.get("upass")
    if uname == "sathya" and upass == "tech":
        request.session["status"] = True
        return redirect("/product/")
    else:
        request.session["status"] = False
        return render(request,"login.html")

