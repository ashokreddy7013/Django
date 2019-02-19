from django.shortcuts import render

def show(request):
    no = 2
    l = [10,20,30]
    about = "This is Sathya's"
    return  render(request,"index.html",{"value":no,"l_value":l,"a_value":about})
