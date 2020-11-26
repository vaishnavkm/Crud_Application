from employee.models import Employee
from django.contrib import admin
from . import models

class employee_list(admin.ModelAdmin):
    list_display = ['eid','ename','eemail','econtact']

# Register your models here.
admin.site.register(Employee,employee_list)
