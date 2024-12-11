from django import forms

class SignUp(forms.Form):
    first_name= forms.CharField(initial="First Name")
    last_name=forms.CharField(initial="Last Name")
    email=forms.EmailField(help_text="Enter a valid eMail address")
    address=forms.CharField(required=False)
    age=forms.IntegerField(required=False)
    password=forms.CharField()