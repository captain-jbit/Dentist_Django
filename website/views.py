from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == "POST":
        #getting the types from html form
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        #Sending emails
        send_mail(
            message_name,#subject
            message,#message
            message_email,#from
            ['pimoto4892@trufilth.com'],#to
            fali_silently=False
            )

        return render(request, 'contact.html', {'message-name':message_name})#return name
    else:
        return render(request, 'contact.html', {})
