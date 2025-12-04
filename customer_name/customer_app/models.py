from django.db import models
from django.contrib import admin
# Create your models here.
class customer(models.Model):
    customer_name=models.CharField(max_length=20)
    customer_id=models.IntegerField(help_text="Enter you id")
    customer_email=models.CharField(help_text="enter your email")
    dob=models.DateField()
class customeradmin(admin.ModelAdmin):
    list_display=['customer_name','customer_id','customer_email','dob']



