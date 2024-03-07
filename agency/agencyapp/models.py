from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Group(models.Model):
    group_name = models.CharField(max_length = 30, unique=True)
    
class Branch(models.Model):
    branch_name = models.CharField(max_length=50, unique=True)
    branch_location = models.CharField(max_length=50)


class User(AbstractUser):
    contact=models.IntegerField(default= 0)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE, default=1)
    location=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    group_id=models.ForeignKey(Group, on_delete=models.CASCADE, default=2)

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=300)
    product_rate = models.IntegerField(default = 0)
    stock = models.IntegerField(default=0)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)

# class ProductStock(models.Model):
#     product_id = models.ForeignKey(Product, on_delete = models.CASCADE)

class Service(models.Model):
    service_name = models.CharField(max_length = 30)
    service_rate = models.IntegerField()
    service_description = models.CharField(max_length = 300)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)

class Bookings(models.Model):
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE, blank = True, null = True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    cost = models.IntegerField()
    booking_type = models.CharField(max_length=30, default='PRODUCT')
    product_qty = models.IntegerField(blank = True, null = True)
    payment_status = models.CharField(max_length = 30)
    delivery_status = models.CharField(max_length = 30)
    work_assigned = models.BooleanField(default = False)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE, blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)

class Work(models.Model):
    work_status = models.CharField(max_length = 30, default = 'ASSIGNED')
    booking_id = models.ForeignKey(Bookings, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at =  models.DateTimeField(auto_now_add = True)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    work_complete_date = models.DateTimeField(blank =True, null = True)
    
    # manager_id = models.ForeignKey(User, on_delete=models.CASCADE)
# class Manager(models.Model):
#     manager_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
class Complaint(models.Model):
    complaint_name = models.CharField(max_length=30)
    complaint_desc = models.CharField(max_length=500)
    user_id = models.ForeignKey(User, on_delete= models.CASCADE, related_name = 'User')
    booking_id = models.ForeignKey(Bookings, on_delete = models.CASCADE)
    status = models.CharField(max_length=30, default='OPEN')
    resolution = models.CharField(max_length = 1000, null = True, blank = True)
    staff_id = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True, related_name = 'Staff')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    read = models.BooleanField(default = True, null = True)