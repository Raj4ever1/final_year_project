from django.shortcuts import render,HttpResponse
from django.forms.models import model_to_dict
from .models import crop,land
from django.contrib.sites.shortcuts import get_current_site
# Create your views here.
def detail(request):
     details={}
     lands=land.objects.all()
     for i in lands:
          details[str(i.name)] =[i.pk]
          for j in crop.objects.all().filter(land_type=str(i.name).lower()):
               details[str(i.name)].append(j)
          print(details[i.name])
     return render(request, 'detail/detail.html',locals())
def land_detail(request,offset):
     a=land.objects.get(pk=offset)
     a=model_to_dict(a)
     a['img']='http://'+get_current_site(request).domain+ a['img'].url
     string = '<div id="content_right_crop">'
     string += '<img src="' + a['img'] + '" width=300 height=300>'
     string +='<br><label>Name: </label> ' + a['name'].title()
     string += '</div>';
     return HttpResponse(string)
def crop_detail(request,offset):
     a=crop.objects.get(pk=offset)
     a=model_to_dict(a)
     a['img']='http://'+get_current_site(request).domain+ a['img'].url
     string = '<div class="content_right_crop"> <div class="cropImg">'
     string +='<img src="' + a['img'] + '" width=300 height=300> </div>'
     string += '<div class="cropInfo"><br><label>Name: </label> ' + a['name'].title()
     string += '<br><label>Climatic Condition: </label> ' + a['climatic_condition'].title()
     string += '<br><label>Water Quantity: </label> ' + a['water_quantity'].replace('-', ' to ') + ' mm'
     string += '<br><label>Moisture: </label> ' + a['moisture']
     string += '<br><label>Pesticides: </label> ' + a['pesticides'].title()
     string += '<br><label>ph level: </label> ' + str(a['ph_level'])
     string += '<br><label>Min temp: </label> ' + str(a['min_temp']) + '&#8451'
     string += '<br><label>Max temp: </label> ' + str(a['max_temp']) + '&#8451'
     string += '<br><label>Description: </label> ' + a['description']
     string += '</div></div>'
     return HttpResponse(string)