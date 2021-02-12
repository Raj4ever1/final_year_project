from django.db import models

# Create your models here.
class crop(models.Model):
    name = models.CharField(max_length=100)
    climatic_condition=models.CharField(max_length=100)
    water_quantity=models.CharField(max_length=100)
    moisture=models.CharField(max_length=100)
    pesticides=models.CharField(max_length=200)
    ph_level=models.FloatField(default=0)
    min_temp=models.FloatField(default=0)
    max_temp=models.FloatField(default=100)
    description=models.TextField(max_length=1000)
    img = models.ImageField(upload_to='crops')
# Create your models here.
