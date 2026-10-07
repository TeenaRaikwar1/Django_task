
from django.db import models
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    salary = models.FloatField()
    address = models.TextField(max_length=200, default='Null')
    Company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
        related_name='employees',
        default=None,
        null=True,
        blank=True
    )
    department = models.ForeignKey(
        'Department',
        on_delete=models.CASCADE,
        related_name='employees',
        default=None,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
class Company(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    location = models.TextField(max_length=50)
    branch_num = models.IntegerField()

    def __str__(self):
        return self.name
class Department(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name
