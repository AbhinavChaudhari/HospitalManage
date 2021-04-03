from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Patient(models.Model):
    
    name = models.CharField(max_length=200)
    adrs = models.CharField(max_length=500)
    email = models.EmailField()
    mobileNo = models.CharField(max_length=20)
    referedBy = models.CharField(max_length=100)
    remark  = models.CharField(max_length=100,null=True,blank=True)    
    total = models.IntegerField()
    method = models.CharField(max_length=50 ,null=True,blank=True)
    trId = models.CharField(max_length=50 ,null=True,blank=True)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)
    

class Tests(models.Model):
    Patient = models.ForeignKey(Patient, on_delete= models.CASCADE)
    Test_name = models.CharField(max_length=500)
    qty = models.PositiveIntegerField()
    t_price = models.FloatField()

    def __str__(self):
        return f"{self.Test_name } |  Qty: {self.qty}"


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True,blank=True)
    mobileNo = models.CharField(max_length=20,null=True,blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    

