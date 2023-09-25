from django.db import models
from django.shortcuts import render 

class User(models.Model): 
    name = models.CharField(max_length=20) 
    email = models.EmailField() 
    phone = models.CharField(max_length=20) 

class Person(models.Model): 
    name = models.CharField(max_length=20) 
    email = models.EmailField() 
    phone = models.CharField(max_length=20) 

class Booking(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)

   

class Menu(models.Model):
    name = models.CharField(max_length=200) 
    price = models.IntegerField(null=False) 
    description = models.TextField(max_length=1000, default='')

    def __str__(self):
        return self.name
    
