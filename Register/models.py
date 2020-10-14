from django.db import models

# Create your models here.


class Employee(models.Model):
    EmpId = models.IntegerField(blank=False, primary_key=True)
    EmpName = models.CharField(blank=False, max_length=50)
    Dept = models.CharField(blank=False, max_length=50)
    Salary = models.IntegerField(blank=False)

    def __str__(self):
        return self.EmpId


class Expenses(models.Model):
    Time = models.DateTimeField(auto_now_add=True)
    EmpId = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Tags = models.CharField(blank=False, max_length=50)
    Amount = models.IntegerField(blank=True)

    def __str__(self):
        return self.EmpId
