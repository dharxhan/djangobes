from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def subscribeuser(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        send_mail("Django Email Concept", message, settings.EMAIL_HOST_USER,['kullollitarun7@gmail.com'], fail_silently=False)

    return render(request, 'subscriber.html')