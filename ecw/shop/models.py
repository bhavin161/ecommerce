from django.db import models

# Create your models here.

class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=30000)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images",default="")


    def __str__(self):
      return self.product_name


class Contact(models.Model):
   mes_id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=50)
   email = models.CharField(max_length=50, default="")
   phone = models.IntegerField(default="")
   desc = models.CharField(max_length=30000 ,default="")

   def __str__(self):
    return self.name


class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    amount = models.IntegerField(default=0)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    address1 = models.CharField(max_length=500, default="")
    address2 = models.CharField(max_length=500, default="")
    city = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=50, default="")
    zip_code = models.IntegerField(max_length=50, default="")
    phone = models.IntegerField(default="")

class OrdersUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id =  models.IntegerField(max_length=50, default="")
    update_desc = models.CharField(max_length=5000, default="")
    timestamp = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.update_desc[0:7]+"..."