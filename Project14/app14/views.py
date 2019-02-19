from django.shortcuts import render
from firebase.firebase import FirebaseApplication

# Create your views here.
def showIndex(request):
    fire = FirebaseApplication("https://djangoproduct.firebaseio.com/", None)
    d1 = fire.get("product", None)
    return render(request, "index.html", {"data": d1})

def saveProduct(request):
    no = request.POST.get("t1")
    name = request.POST.get("t2")
    price = request.POST.get("t3")

    fire = FirebaseApplication("https://djangoproduct.firebaseio.com/",None)
    fire.put("product",no,{"name":name,"price":price})
    d1 = fire.get("product",None)
    return render(request,"index.html",{"data":d1})


def deleteProduct(request):
    pno = request.POST.get("dp")
    fire = FirebaseApplication("https://djangoproduct.firebaseio.com/", None)
    fire.delete("product",pno)
    d1 = fire.get("product", None)
    return render(request, "index.html", {"data": d1})


def updateProduct(request):
    pno = request.GET.get("up")
    fire = FirebaseApplication("https://djangoproduct.firebaseio.com/", None)
    d1 = fire.get("product",pno)
    d1["no"] = pno
    return render(request,"index.html",d1)