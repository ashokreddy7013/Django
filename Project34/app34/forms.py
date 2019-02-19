
from django import forms

class MyRegisterForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    contact = forms.IntegerField()

