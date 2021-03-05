from django.urls import path,re_path
from . import views
urlpatterns = [
    path('',views.detail,name='detail'),
    #re_path('(?P<offset>\d{0,4})/$',views.crop_detail)
    re_path('crop/(?P<offset>\d{0,4})/$',views.crop_detail),
    re_path('land/(?P<offset>\d{0,4})/$',views.land_detail)
]