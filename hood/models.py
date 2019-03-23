
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q
import datetime as dt


# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='hoods/', null=True)
    neighbourhood_count= models.IntegerField(default=0, null=True, blank=True)
   
    def __str__(self):
        return self.name

    def save_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls,Neighbourhood):
        cls.objects.filter(Neighbourhood=Neighbourhood).delete()


class News(models.Model):
    title = models.CharField(max_length=100)
    notification = HTMLField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood_id = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Healthservices(models.Model):
    healthservices = models.CharField(max_length=100)

    def __str__(self):
        return self.healthservices

    def save_healthservices(self):
        self.save()

    @classmethod
    def delete_healthservices(cls,healthservices):
        cls.objects.filter(healthservices=healthservices).delete()


class Business(models.Model):
    business_name = models.CharField(max_length=30, null=True)
    image = models.ImageField(upload_to='images/', null=True)
    description = models.CharField(max_length=1000, null = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="business")
    neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE,related_name="neighbourhoodbusiness",null=True,blank=True)
    contact = models.IntegerField()
    business_email = models.CharField(max_length=200, null = True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.business_name

class Health(models.Model):
    health_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True)
    neighbourhood_id = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    email = models.EmailField()
    contact = models.IntegerField()
   

    def __str__(self):
        return self.health_name

class Authorities(models.Model):
    authority_name =models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True)
    neighbourhood_id = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    email = models.EmailField()
    contact = models.IntegerField()

   

    def __str__(self):
        return self.authority_name


class Profile(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='pics/')
    bio = models.CharField(max_length=100)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)

    

    def save_profile(self):
        self.save()