from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
import json
from django.forms.models import model_to_dict

# Create your views here.
def profile(request):
    data={}
    object=model_to_dict(User.objects.get(pk=request.user.id))
    for i in ['username','first_name','last_name','email']:data[i]=object[i]
    return render(request,'userprofile/userprofile.html',{'data':data})