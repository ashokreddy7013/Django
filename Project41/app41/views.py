from django.shortcuts import render
from django.http import HttpResponse
from app41.functions.functions import handle_uploaded_file
from app41.form import StudentForm

def index(request):
    student = StudentForm(request.POST, request.FILES)
    if student.is_valid():
        handle_uploaded_file(request.FILES['file'])
        return HttpResponse("File uploaded successfuly")
    else:
        student = StudentForm()
        return render(request,"index.html",{'form':student})
