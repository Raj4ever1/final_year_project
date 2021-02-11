from django.shortcuts import render
from .models import crop
# Create your views here.
def detail(request):
    crops=crop.objects.all()
    return render(request, 'detail/detail.html',locals())