from django.contrib import admin
from application.models import EmployeeModel

# Register your models here.
class AdminModel(admin.ModelAdmin):
    list_display = ['employee_id','first_name','last_name','email','phone']
admin.site.register(EmployeeModel,AdminModel)

