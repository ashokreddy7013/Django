
from django.http import HttpResponse
from django.views.generic import View
from .models import Employee
import csv
from reportlab.pdfgen import canvas

class OpenCSV(View):
    def post(self,request):
        response = HttpResponse(content_type="text/csv")
        response['Content-Disposition'] = 'attachment;filename="mydata.csv"'
        emp = Employee.objects.all()
        write = csv.writer(response)
        for x in emp:
            write.writerow([x.idno,x.name,x.salary,x.designation])

        return response

class OpenPDF(View):
    def post(self,request):
        response = HttpResponse(content_type="application/pdf")
        response['Content-Disposition'] = 'attachment;filename="mydata.pdf"'

        emp = Employee.objects.all()
        text = ""
        for x in emp:
            text+=str(x.idno)+"  "+x.name+"  "+str(x.salary)+"  "+x.designation+"\n"

        p = canvas.Canvas(response)
        p.drawString(100,200,text)
        p.showPage()
        p.save()
        return  response