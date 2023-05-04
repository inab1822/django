from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=20)
    des_eng = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    img_path = models.CharField(max_length=255,blank=True)
    
    def __str__(self):
        return self.name