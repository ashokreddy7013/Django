from django.shortcuts import render
from django.core.mail import send_mail
from Project46 import settings as se


# def send(request):
#     to = request.POST.get("to")
#     subject = request.POST.get("sub")
#     message = request.POST.get("message")
#
#     emails = list(to.split(','))
#     send_mail(subject=subject,message=message,from_email=se.EMAIL_HOST_USER,recipient_list=emails)
#     return render(request,"index.html",{"message":"Mail Sent"})

from django.core.mail import EmailMessage

def send(request):
    to = request.POST.get("to")
    subject = request.POST.get("sub")
    message = request.POST.get("message")
    emails = list(to.split(','))
    em = EmailMessage(subject,message,se.EMAIL_HOST_USER,emails)
    em.send(False)
    return render(request, "index.html", {"message": "Mail Sent"})


