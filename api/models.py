from django.db import models

# Create your models here.

class Department(models.Model):
    dep_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    dep_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name