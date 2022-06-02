from django.db import models
from django.db.models.base import Model
from django.db.models.fields import AutoField, PositiveIntegerRelDbTypeMixin
#from django.http.request import UploadHandlerList

class Product(models.Model) :
    product_id = models.AutoField
    product_name = models.CharField(max_length=80)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    Price = models.IntegerField(default=0)
    desc = models.CharField(max_length=200)
    pub_date = models.DateField()
    image = models.ImageField(upload_to ='shop/images', default="")

    def __str__(self) :
        return self.product_name

class Contact(models.Model) :
    msg_id = models.AutoField(primary_key=True)
    Firstname = models.CharField(max_length=80)
    Email = models.CharField(max_length=50,default="")
    Address = models.CharField(max_length=50,default="")
    State = models.CharField(max_length=50,default="")
    Lastname = models.CharField(max_length=50,default="")
    City = models.CharField(max_length=20,default="")
    phonenumber = models.IntegerField(default=0)
    Query = models.CharField(max_length=400)
    
    def __str__(self) :
        return self.Firstname

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000,default="")
    name =  models.CharField(max_length=100,default="")
    email =  models.CharField(max_length=100,default="")
    phonenumber =  models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    address1 =  models.CharField(max_length=100,default="")
    address2 =  models.CharField(max_length=100,default="")
    city =  models.CharField(max_length=100,default="")
    state =  models.CharField(max_length=100,default="")
    zip_code =  models.CharField(max_length=100,default="")

class orderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamps = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.update_desc[0:7]+"..."