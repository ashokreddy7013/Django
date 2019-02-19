from django.shortcuts import render
from django.views.generic import RedirectView


class OpenFacebook(RedirectView):
    url = 'http://www.facebook.com'