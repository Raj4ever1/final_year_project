from django.shortcuts import render,HttpResponse
import json
from django.forms.models import model_to_dict
from .models import crop
# Create your views here.
def detail(request):
    crops=crop.objects.all()
    return render(request, 'detail/detail.html',locals())
def crop_detail(request,offset):
     a=crop.objects.get(pk=offset)
     a=model_to_dict(a)
     a['img']=a['img'].url
     data=json.dumps(a)
     return HttpResponse(data)