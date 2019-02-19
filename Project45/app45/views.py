from django.http import HttpResponse
from django.core.mail import send_mail
from Project45 import settings as se

# Create your views here.
def sendmail(request):
    send_mail("Check", "This is a check mail", se.EMAIL_HOST_USER,
              ["mailmenaveenkumar@gmail.com"])
    return HttpResponse("Mail Sent")
