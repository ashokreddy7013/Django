from django.shortcuts import render

from django.views.generic import View

names = ["Ravi","kumar","krishna","mohan","rama"]

class Search(View):
    def post(self,request):
        name = request.POST.get("t1")
        if name in names:
            return render(request,"index.html",{"message":"Available"})
        else:
            return render(request, "index.html", {"message": "Not-Available"})

