from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class contactteam(models.Model):
    cname=models.CharField(max_length=250)
    cimg=models.ImageField(upload_to='pics')
    cdesc=models.TextField()

    def __str__(self):
        return self.cname