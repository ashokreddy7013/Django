
from django import forms

my_years = (1880,1881,1882,1883)

class Registration(forms.Form):
    name = forms.CharField(label="Enter Name")
    age = forms.IntegerField(label="Enter Age")
    contactno = forms.IntegerField(label="Enter Contact No")
    email = forms.EmailField(label="Enter Email-Id")
    password = forms.CharField(label="Enter Password",widget=forms.PasswordInput)
    dob = forms.DateField(label="Date of Birth",
                          widget=forms.SelectDateWidget(years=my_years))