from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    employee_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"