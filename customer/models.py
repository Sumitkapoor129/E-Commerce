from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Customer(AbstractUser):
    profile_pic=models.ImageField(upload_to=f'customer_image', blank=True)
    
class Product(models.Model):
    owner=models.ForeignKey(Customer , on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=9,decimal_places=2)
    quantity=models.SmallIntegerField()
    image=models.ImageField(upload_to=f'product_image', blank=True)
    description=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user_id=models.IntegerField(default=0)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.SmallIntegerField() 
    created_at=models.DateTimeField(auto_now_add=True)
    def total_price(self):
        return self.product.price*self.quantity
    
class Orders(models.Model):
    user_id=models.IntegerField()
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.SmallIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.TextField(default="Confirmed")
    def total_price(self):
        return self.product.price*self.quantity
    
    
        
    
