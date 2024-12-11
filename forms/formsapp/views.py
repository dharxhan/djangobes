from django.shortcuts import render
from . import forms

# Create your views here.
def regform(request):
    form= forms.SignUp()
    if request.method == "POST":
        form=forms.SignUp(request.POST)
        html="We have received the form again"
    else:
        html="Welcome first time"
    return render(request, 'signup.html', {'html' : html, 'form': form})