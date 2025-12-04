from django.contrib import admin
from .models import (customer,customeradmin)
# Register your models here.
admin.site.register(customer,customeradmin)