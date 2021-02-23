from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import contact
from threading import Thread
from django.core.mail import EmailMessage
# Create your views here.
def contacts(request):
     con=contact.objects.all()
     return render(request,'contact/contact.html',locals())


def contact_detail(request,offset):
     a=contact.objects.get(pk=offset)
     return HttpResponse(a.name)
def feedback(request):
     def feedbacksend():
          string = request.POST['feedback'].strip()
          if string:
               email_body = string + f'\n from {request.user.username}'
               EmailMessage(
                    'Feedback',
                    email_body,
                    'Digital Farming',
                    ['riswitha@gmail.com']
               ).send(fail_silently=False)
     Thread(target=feedbacksend).start()
     return redirect('contacts')