from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
