from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name=models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    photo=models.ImageField(upload_to='images')
    department = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
